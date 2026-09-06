import os
import random
from models.item import Item
from models.room import Room
from models.player import Player

# --- POLUT JA ASETUKSET ---
# Lukitsee kansion aina suoraan tämän scriptin omaan kansioon:
SKRIPTIN_KANSIO = os.path.dirname(os.path.abspath(__file__))
DATA_KANSIO = os.path.join(SKRIPTIN_KANSIO, "data")

INTRO_POLKU = os.path.join(DATA_KANSIO, "intro.txt")
OHJEET_POLKU = os.path.join(DATA_KANSIO, "instructions.txt")
TALLENNUS_POLKU = os.path.join(DATA_KANSIO, "savegame.txt")

LÖYDÖT = [
    {"nimi": "Harmaa kivi", "paino_kg": 2.0, "min_syvyys": 1, "painokerroin": 60, "viesti": "Murskasit seinän, mutta käteesi jäi vain tavallista kiveä."},
    {"nimi": "Kivihiili", "paino_kg": 1.5, "min_syvyys": 1, "painokerroin": 25, "viesti": "Musta suoni paljastuu murtuneen kiven takaa. Löysit kivihiiltä!"},
    {"nimi": "Rautamalmi", "paino_kg": 4.0, "min_syvyys": 2, "painokerroin": 15, "viesti": "Kivi kimmeltää ruskehtavana. Sait palan rautamalmia!"},
    {"nimi": "Kultaesiintymä", "paino_kg": 1.0, "min_syvyys": 3, "painokerroin": 8, "viesti": "Kallion raosta pilkahtaa kirkas kultainen kimallus!"},
    {"nimi": "Timantti", "paino_kg": 0.2, "min_syvyys": 4, "painokerroin": 2, "viesti": "Hakkusi osuu johonkin kovaan! Sininen valo heijastuu seinästä: LÖYSIT TIMANTIN!"}
]

VASTASUUNNAT = {
    "pohjoinen": "etela",
    "etela": "pohjoinen",
    "ita": "lansi",
    "lansi": "ita",
    "alas": "ylos",
    "ylos": "alas"
}

SUUNTA_LYHENTEET = {
    "p": "pohjoinen",
    "e": "etela",
    "i": "ita",
    "l": "lansi",
    "a": "alas",
    "y": "ylos"
}




def alusta_tekstitiedostot():
    """Luo data-kansion ja perustekstit, jos niitä ei ole vielä olemassa."""
    os.makedirs(DATA_KANSIO, exist_ok=True)
    
    if not os.path.exists(INTRO_POLKU):
        with open(INTRO_POLKU, "w", encoding="utf-8") as f:
            f.write("=== TERVETULOA KAIVOKSEEN ===\n"
                    "Olet saapunut hylättyyn luolastoon etsimään arvokkaita rikkauksia.\n"
                    "Louhi uusia tunneleita ja kerää malmit talteen!")

    if not os.path.exists(OHJEET_POLKU):
        with open(OHJEET_POLKU, "w", encoding="utf-8") as f:
            f.write("=== OHJEET ===\n"
                    "- Liiku valmiissa tunneleissa tai louhi hakkua heiluttaen uusia reittejä.\n"
                    "- Seinän murtaminen vie 10 energiaa ja tuottaa esineen maahan.\n"
                    "- Muista poimia maassa kimmeltävät esineet reppuusi!\n"
                    "- Lepää nuotiolla, kun energiasi käy vähiin.")


def lue_tiedosto(polku: str) -> str:
    """Lukee tekstitiedoston sisällön."""
    if os.path.exists(polku):
        with open(polku, "r", encoding="utf-8") as f:
            return f.read().strip()
    return f"Tiedostoa {polku} ei löytynyt."


def tallenna_peli(pelaaja: Player):
    """Tallentaa pelaajan tiedot, huoneen ja inventaarion tiedostoon."""
    os.makedirs(DATA_KANSIO, exist_ok=True)
    with open(TALLENNUS_POLKU, "w", encoding="utf-8") as f:
        # Rivimuoto: Nimi;Energia;X;Y;Syvyys;HuoneenNimi
        f.write(f"{pelaaja.name};{pelaaja.energia};{pelaaja.x};{pelaaja.y};{pelaaja.syvyys};{pelaaja.location.name}\n")
        # Tallennetaan repun esineet: nimi;paino
        for item in pelaaja.items:
            f.write(f"{item.name};{item.weight}\n")
    print(f"\n[+] Peli tallennettu tiedostoon: {TALLENNUS_POLKU}")


def lataa_peli() -> Player | None:
    """Lataa tallennetun pelin savegame.txt-tiedostosta."""
    if not os.path.exists(TALLENNUS_POLKU):
        return None

    try:
        with open(TALLENNUS_POLKU, "r", encoding="utf-8") as f:
            rivit = [r.strip() for r in f.readlines() if r.strip()]

        if not rivit:
            return None

        kentat = rivit[0].split(";")
        nimi = kentat[0]
        energia = int(kentat[1])
        x = int(kentat[2])
        y = int(kentat[3])
        syvyys = int(kentat[4])
        huoneen_nimi = kentat[5]

        huone = Room(huoneen_nimi)
        pelaaja = Player(nimi, huone)
        pelaaja.energia = energia
        pelaaja.x = x
        pelaaja.y = y
        pelaaja.syvyys = syvyys

        for item_rivi in rivit[1:]:
            parts = item_rivi.split(";")
            if len(parts) == 2:
                pelaaja.items.append(Item(parts[0], float(parts[1])))

        return pelaaja
    except Exception as e:
        print(f"\nVirhe tallennuksen lukemisessa: {e}")
        return None




def louhi_ja_liiku(pelaaja: Player):
    """Louhii uuden huoneen tai siirtyy olemassa olevaan, jos seinä on jo auki."""
    if pelaaja.energia < 10:
        print("\nOlet liian poikki heiluttamaan hakkua! Lepää hetki nuotiolla.")
        return

    suunta_syote = input("\nMihin suuntaan haluat louhia? (pohjoinen / etela / ita / lansi / alas): ").strip().lower()
    suunta = SUUNTA_LYHENTEET.get(suunta_syote, suunta_syote)

    if suunta not in ["pohjoinen", "etela", "ita", "lansi", "alas"]:
        print("Tuntematon suunta.")
        return

    # Jos suuntaan on jo kaivettu tunneli, liikutaan sinne suoraan
    if suunta in pelaaja.location.exits:
        print("\nTähän suuntaan on jo avoin tunneli! Siirrytään sinne...")
        pelaaja.move(pelaaja.location.exits[suunta])
        _paivita_koordinaatit(pelaaja, suunta)
        return

    # Louhitaan uusi huone
    pelaaja.energia -= 10
    print("\n*KLIK-KLANG* Isket hakulla kalliota ja murrat reitin eteenpäin...")

    _paivita_koordinaatit(pelaaja, suunta)
    if suunta == "alas":
        print(f"Kaivoit kuilun syvemmälle! Olet nyt syvyystasolla {pelaaja.syvyys}.")

    # Luodaan uusi Room-olio ja kytketään ovet kahteen suuntaan
    uusi_huone = Room(f"Kammio [{pelaaja.x}, {pelaaja.y}] S{pelaaja.syvyys}")
    pelaaja.location.add_exit(suunta, uusi_huone)
    uusi_huone.add_exit(VASTASUUNNAT[suunta], pelaaja.location)

    # UML-metodi: move
    pelaaja.move(uusi_huone)

    # Arvotaan löytö syvyystason mukaan
    mahdolliset = [l for l in LÖYDÖT if pelaaja.syvyys >= l["min_syvyys"]]
    painot = [l["painokerroin"] for l in mahdolliset]
    saalis = random.choices(mahdolliset, weights=painot, k=1)[0]

    print(saalis["viesti"])
    
    # Asetetaan malmi huoneen esineeksi (UML: Room -> item: Item)
    uusi_huone.item = Item(saalis["nimi"], saalis["paino_kg"])
    print("Vinkki: Esine jäi maahan. Käytä toimintoa 3 poimiaksesi sen reppuun!")


def _paivita_koordinaatit(pelaaja: Player, suunta: str):
    if suunta == "pohjoinen": pelaaja.y += 1
    elif suunta == "etela": pelaaja.y -= 1
    elif suunta == "ita": pelaaja.x += 1
    elif suunta == "lansi": pelaaja.x -= 1
    elif suunta == "alas": pelaaja.syvyys += 1


def poimi_esine_maasta(pelaaja: Player):
    """Käyttää Player-luokan UML-metodia collect_item()"""
    esine = pelaaja.collect_item()
    if esine:
        print(f"\nPoimit maasta esineen: {esine.name} ({esine.weight:.1f} kg)")
    else:
        print("\nTämän kammiotilan lattialla ei ole mitään poimittavaa.")


def lisaa_esine_manuaalisesti(pelaaja: Player):
    """Tehtävänannon vaatimus vapaan syötteen lisäämisestä reppuun."""
    nimi = input("\nKirjoita esineen nimi, jonka haluat heittää reppuun: ").strip()
    if nimi:
        pelaaja.items.append(Item(nimi, 1.0))
        print(f"'{nimi}' laitettiin reppuun talteen.")
    else:
        print("Et antanut kelvollista esinettä.")


def nayta_reppu(pelaaja: Player):
    """Tulostaa pelaaja-olion items-listan sisällön."""
    print("\n--- REPUN SISÄLTÖ ---")
    if not pelaaja.items:
        print("Reppusi on tyhjä.")
    else:
        for nro, esine in enumerate(pelaaja.items, 1):
            print(f"{nro}. {esine}")
        print(f"Kokonaispaino: {pelaaja.get_total_weight():.1f} kg")
    print("---------------------")


def nayta_tiedot(pelaaja: Player):
    print("\n--- PELAAJAN TILA ---")
    print(f"Nimi: {pelaaja.name}")
    print(f"Sijainti: {pelaaja.location.name}")
    print(f"Koordinaatit: X={pelaaja.x}, Y={pelaaja.y} (Syvyystaso: {pelaaja.syvyys})")
    print(f"Energia: {pelaaja.energia} / 100")
    print("---------------------")


def lepaa(pelaaja: Player):
    pelaaja.energia = 100
    print("\nIstahdit nuotion ääreen syömään eväitä. Energiasi palautui sataan!")




def main():
    alusta_tekstitiedostot()
    print(lue_tiedosto(INTRO_POLKU))

    pelaaja = None
    aloitushuone = Room("Kaivoksen suuaukko [0, 0] S1")

    # Kysytään tallennuksen lataamista, jos tiedosto löytyy
    if os.path.exists(TALLENNUS_POLKU):
        valinta = input("\nLöydettiin aiempi tallennus! Haluatko jatkaa sitä? (k/e): ").strip().lower()
        if valinta in ("k", "kylla", "y"):
            pelaaja = lataa_peli()
            if pelaaja:
                print(f"\nTervetuloa takaisin, {pelaaja.name}!")

    # Jos ei ladattu, luodaan uusi pelaaja
    if not pelaaja:
        nimi = input("\nAnna kaivosmiehen nimi: ").strip()
        while True:
            try:
                ika = int(input("Anna ikä: "))
                break
            except ValueError:
                print("Syötä numero.")

        if ika < 12:
            print("Et pääse vielä alas kaivokseen. Tule takaisin kun olet vanhempi!")
            return

        pelaaja = Player(nimi if nimi else "Kaivosmies", aloitushuone)
        print(f"\nTervetuloa syvyyksiin, {pelaaja.name}!")

    print("\n" + lue_tiedosto(OHJEET_POLKU))

    while True:
        nykyinen = pelaaja.location
        print("\n==========================================")
        print(f"HUONE: {nykyinen.name}")
        print(nykyinen.get_map_view())
        if nykyinen.item:
            print(f"Lattialla kimmeltää: {nykyinen.item.name} ({nykyinen.item.weight:.1f} kg)")
        print(f"Energia: {pelaaja.energia} / 100")
        print("==========================================")

        print("1. Louhi tietä eteenpäin (Liiku / Kaiva)")
        print("2. Tarkastele reppua")
        print("3. Poimi esine maasta (collect_item)")
        print("4. Lisää esine manuaalisesti (tehtävävaatimus)")
        print("5. Katso tilanne ja koordinaatit")
        print("6. Lepää ja palauta energia")
        print("7. Tallenna peli")
        print("8. Poistu kaivoksesta")

        valinta = input("Valitse toiminto (1-8): ").strip()

        match valinta:
            case "1":
                louhi_ja_liiku(pelaaja)
            case "2":
                nayta_reppu(pelaaja)
            case "3":
                poimi_esine_maasta(pelaaja)
            case "4":
                lisaa_esine_manuaalisesti(pelaaja)
            case "5":
                nayta_tiedot(pelaaja)
            case "6":
                lepaa(pelaaja)
            case "7":
                tallenna_peli(pelaaja)
            case "8":
                print("\nKiipesit tikkaat ylös päivänvaloon. Peli päättyi!")
                break
            case _:
                print("Virheellinen valinta! Valitse numero väliltä 1-8.")


if __name__ == "__main__":
    main()