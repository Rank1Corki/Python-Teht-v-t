import os
import random
from models.item import Item
from models.room import Room
from models.player import Player

SKRIPTIN_KANSIO = os.path.dirname(os.path.abspath(__file__))
DATA_KANSIO = os.path.join(SKRIPTIN_KANSIO, "data")

INTRO_POLKU = os.path.join(DATA_KANSIO, "intro.txt")
OHJEET_POLKU = os.path.join(DATA_KANSIO, "instructions.txt")
TALLENNUS_POLKU = os.path.join(DATA_KANSIO, "savegame.txt")

# Kestävän kehityksen ja kaivauksen materiaalit
LÖYDÖT = [
    {
        "nimi": "Kivimurska",
        "paino_kg": 2.0,
        "kategoria": "materiaali",
        "min_syvyys": 1,
        "painokerroin": 50,
        "viesti": "Murskasit kiveä. Maahan jää tiivistä kiviainesta maaperän vahvistamiseen."
    },
    {
        "nimi": "Vanha myrkkytynnyri",
        "paino_kg": 5.0,
        "kategoria": "jate",
        "min_syvyys": 1,
        "painokerroin": 25,
        "viesti": "Löysit vanhan hylätyn kemikaalitynnyrin, joka uhkaa vuotaa pohjaveteen!"
    },
    {
        "nimi": "Rautamalmi",
        "paino_kg": 4.0,
        "kategoria": "materiaali",
        "min_syvyys": 2,
        "painokerroin": 20,
        "viesti": "Kalliosta paljastuu uusiutuvaan akkutuotantoon sopivaa rautamalmia."
    },
    {
        "nimi": "Litiumsuoni",
        "paino_kg": 1.5,
        "kategoria": "materiaali",
        "min_syvyys": 2,
        "painokerroin": 15,
        "viesti": "Löysit arvokasta litiumia energiantuotannon akkuihin!"
    },
    {
        "nimi": "Kallionäyte",
        "paino_kg": 0.5,
        "kategoria": "tutkimus",
        "min_syvyys": 3,
        "painokerroin": 10,
        "viesti": "Löysit harvinaisen kallioperänäytteen geologista tutkimusta varten."
    }
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


def alusta_tekstitiedostot() -> None:
    """Luo pelin tarvitseman kansiorakenteen ja aloitusohjeet tarvittaessa."""
    os.makedirs(DATA_KANSIO, exist_ok=True)

    if not os.path.exists(INTRO_POLKU):
        with open(INTRO_POLKU, "w", encoding="utf-8") as f:
            f.write(
                "=== OPERAATIO PUHDAS MAAPERÄ ===\n"
                "Olet saapunut vanhalle hylätylle kaivokselle ympäristötutkijana.\n"
                "Tavoitteesi on ennallistaa alue ja viedä maaliin yksi kolmesta ratkaisusta:\n"
                " 1. Rakenna aurinkosähköaseman akusto (Litiumsuoni + Rautamalmi)\n"
                " 2. Suojaa pohjavesi keräämällä vaaralliset jätteet (2 kpl Vanha myrkkytynnyri)\n"
                " 3. Ennallista syvänteen luonto (2 kpl Kivimurska + 1 kpl Kallionäyte)\n"
            )

    if not os.path.exists(OHJEET_POLKU):
        with open(OHJEET_POLKU, "w", encoding="utf-8") as f:
            f.write(
                "=== PELIOHJEET ===\n"
                "- Liiku olemassa olevissa huoneissa tai louhi uusia suuntia.\n"
                "- Louhinta kuluttaa 10 yksikköä energiaa ja paljastaa materiaaleja.\n"
                "- Voit levätä palauttaaksesi energiasi tutkimusasemalla.\n"
                "- Muista kerätä maassa olevat materiaalit reppuun ratkaisua varten.\n"
            )


def lue_tiedosto(polku: str) -> str:
    """Lukee annetussa tiedostopolussa olevan sisällön merkkijonona."""
    if os.path.exists(polku):
        with open(polku, "r", encoding="utf-8") as f:
            return f.read().strip()
    return f"Tiedostoa {polku} ei löytynyt."


def tallenna_peli(pelaaja: Player) -> bool:
    """Tallentaa pelaajan tiedot ja repun sisällön tiedostoon."""
    try:
        os.makedirs(DATA_KANSIO, exist_ok=True)
        with open(TALLENNUS_POLKU, "w", encoding="utf-8") as f:
            f.write(f"{pelaaja.name};{pelaaja.age};{pelaaja.energia};{pelaaja.x};{pelaaja.y};{pelaaja.syvyys};{pelaaja.location.name}\n")
            for item in pelaaja.items:
                f.write(f"{item.name};{item.weight};{item.category}\n")
        print(f"\nPeli tallennettu onnistuneesti tiedostoon: {TALLENNUS_POLKU}")
        return True
    except OSError as e:
        print(f"Tallennus epäonnistui: {e}")
        return False


def lataa_peli() -> Player | None:
    """Lataa tallennetun pelin tilan tiedostosta ja palauttaa Player-olion."""
    if not os.path.exists(TALLENNUS_POLKU):
        return None

    try:
        with open(TALLENNUS_POLKU, "r", encoding="utf-8") as f:
            rivit = [r.strip() for r in f.readlines() if r.strip()]

        if not rivit:
            return None

        perustiedot = rivit[0].split(";")
        nimi = perustiedot[0]
        ika = int(perustiedot[1])
        energia = int(perustiedot[2])
        x = int(perustiedot[3])
        y = int(perustiedot[4])
        syvyys = int(perustiedot[5])
        huoneen_nimi = perustiedot[6]

        huone = Room(huoneen_nimi)
        pelaaja = Player(nimi, ika, huone)
        pelaaja.energia = energia
        pelaaja.x = x
        pelaaja.y = y
        pelaaja.syvyys = syvyys

        for item_rivi in rivit[1:]:
            osat = item_rivi.split(";")
            if len(osat) >= 2:
                kategoria = osat[2] if len(osat) > 2 else "materiaali"
                pelaaja.items.append(Item(osat[0], float(osat[1]), kategoria))

        return pelaaja
    except (ValueError, IndexError, OSError) as e:
        print(f"Virhe tallennuksen latauksessa: {e}")
        return None


def paivita_koordinaatit(pelaaja: Player, suunta: str) -> None:
    """Päivittää pelaajan sijaintikoordinaatit liikkumissuunnan perusteella."""
    if suunta == "pohjoinen":
        pelaaja.y += 1
    elif suunta == "etela":
        pelaaja.y -= 1
    elif suunta == "ita":
        pelaaja.x += 1
    elif suunta == "lansi":
        pelaaja.x -= 1
    elif suunta == "alas":
        pelaaja.syvyys += 1
    elif suunta == "ylos" and pelaaja.syvyys > 1:
        pelaaja.syvyys -= 1


def louhi_ja_liiku(pelaaja: Player) -> None:
    """Mahdollistaa siirtymisen tai uuden huoneen louhimisen kartalle."""
    if pelaaja.energia < 10:
        print("\nEnergia on liian alhainen heiluttamaan hakkua! Lepää hetki nuotiolla.")
        return

    suunta_syote = input("\nMihin suuntaan haluat liikkua/louhia? (pohjoinen/etela/ita/lansi/alas/ylos): ").strip().lower()
    suunta = SUUNTA_LYHENTEET.get(suunta_syote, suunta_syote)

    if suunta not in VASTASUUNNAT:
        print("Tuntematon suunta.")
        return


    if suunta in pelaaja.location.exits:
        print("\nReitti on jo valmiina, siirrytään käytävää pitkin...")
        pelaaja.move(pelaaja.location.exits[suunta])
        paivita_koordinaatit(pelaaja, suunta)
        return

    pelaaja.energia -= 10
    print("\nIsket hakulla kalliota ja murrat reitin eteenpäin...")

    _paivita_koordinaatit(pelaaja, suunta)
    if suunta == "alas":
        print(f"Kaivoit kuilun syvemmälle! Olet nyt syvyystasolla {pelaaja.syvyys}.")


    uusi_huone = Room(f"Kammio [{pelaaja.x}, {pelaaja.y}] S{pelaaja.syvyys}")
    pelaaja.location.add_exit(suunta, uusi_huone)
    uusi_huone.add_exit(VASTASUUNNAT[suunta], pelaaja.location)


    pelaaja.move(uusi_huone)


    mahdolliset = [l for l in LÖYDÖT if pelaaja.syvyys >= l["min_syvyys"]]
    painot = [l["painokerroin"] for l in mahdolliset]
    saalis = random.choices(mahdolliset, weights=painot, k=1)[0]

    print(saalis["viesti"])
    

    uusi_huone.item = Item(saalis["nimi"], saalis["paino_kg"])
    print("Vinkki: Esine jäi maahan. Käytä toimintoa 3 poimiaksesi sen reppuun!")


def _paivita_koordinaatit(pelaaja: Player, suunta: str):
    if suunta == "pohjoinen": pelaaja.y += 1
    elif suunta == "etela": pelaaja.y -= 1
    elif suunta == "ita": pelaaja.x += 1
    elif suunta == "lansi": pelaaja.x -= 1
    elif suunta == "alas": pelaaja.syvyys += 1


def poimi_esine_maasta(pelaaja: Player):
    esine = pelaaja.collect_item()
    if esine:
        print(f"\nPoimit reppuun kohteen: {esine.name} ({esine.weight:.1f} kg)")
    else:
        print("\nTässä huoneessa ei ole mitään poimittavaa.")


def lisaa_esine_manuaalisesti(pelaaja: Player):
    nimi = input("\nKirjoita esineen nimi, jonka haluat heittää reppuun: ").strip()
    if nimi:
        pelaaja.items.append(Item(f"Muistiinpano: {nimi}", 0.1, "muistiinpano"))
        print(f"Muistiinpano '{nimi}' lisätty kenttäpäiväkirjaan.")
    else:
        print("Merkintä ei voi olla tyhjä.")


def nayta_reppu(pelaaja: Player):
    """Tulostaa pelaajan items-listan sisällön."""
    print("\n--- REPUN SISÄLTÖ ---")
    if not pelaaja.items:
        print("Reppusi on tyhjä.")
    else:
        for indeksi, esine in enumerate(pelaaja.items, 1):
            print(f"{indeksi}. {esine} [{esine.category}]")
        print(f"Yhteispaino: {pelaaja.get_total_weight():.1f} kg")
    print("---------------------------")


def tulosta_tiedot(pelaaja: Player) -> None:
    """Tulostaa pelaajan perustiedot, koordinaatit ja energian."""
    print("\n--- TUTKIJAN TILA ---")
    print(f"Nimi: {pelaaja.name} (Ikä: {pelaaja.age})")
    print(f"Sijainti: {pelaaja.location.name}")
    print(f"Koordinaatit: X={pelaaja.x}, Y={pelaaja.y}, Syvyystaso={pelaaja.syvyys}")
    print(f"Energia: {pelaaja.energia} / 100")
    print("---------------------")


def lepaa(pelaaja: Player) -> None:
    """Palauttaa pelaajan energian täyteen."""
    pelaaja.energia = 100
    print("\nLepäsit tukikohdassa. Energiasi on jälleen 100!")


def pyyda_pelaajan_tiedot() -> tuple[str, int]:
    """Kysyy pelaajan nimen ja iän"""
    nimi = input("\nAnna tutkijan nimi: ").strip()
    if not nimi:
        nimi = "Tutkija"

    while True:
        try:
            ika = int(input("Anna ikä: "))
            if ika < 12:
                print("Peli on suunnattu vähintään 12-vuotiaille turvallisuussyistä.")
                continue
            return nimi, ika
        except ValueError:
            print("Syötä ikä kokonaislukuna.")


def main() -> None:
    """Pelin pääohjelma"""
    alusta_tekstitiedostot()
    print(lue_tiedosto(INTRO_POLKU))

    pelaaja = None
    aloitushuone = Room("Kaivoksen tukikohta [0, 0] Syvyys 1")

    # Kysytään haluaako pelaaja käyttää vanhaa tallennusta
    if os.path.exists(TALLENNUS_POLKU):
        valinta = input("\nLöydettiin aiempi tallennus. Ladataanko se? (k/e): ").strip().lower()
        if valinta in ("k", "kylla", "y"):
            pelaaja = lataa_peli()
            if pelaaja:
                print(f"\nTervetuloa takaisin kentälle, {pelaaja.name}!")

    # Jos ei ole vanhaa tallenusta
    if not pelaaja:
        nimi, ika = pyyda_pelaajan_tiedot()
        pelaaja = Player(nimi, ika, aloitushuone)
        print(f"\nTervetuloa tutkimusalueelle, {pelaaja.name}!")

    print("\n" + lue_tiedosto(OHJEET_POLKU))

    # Pääsilmukka
    while True:
        nykyinen = pelaaja.location
        print("\n==========================================")
        print(f"SIJAINTI: {nykyinen.name}")
        print(nykyinen.get_map_view())
        if nykyinen.item:
            print(f"Havaitset kohteessa: {nykyinen.item.name} ({nykyinen.item.weight:.1f} kg)")
        print(f"Energia: {pelaaja.energia} / 100")
        print("==========================================")

        print("1. Louhi tietä eteenpäin (Liiku / Kaiva)")
        print("2. Tarkastele reppua")
        print("3. Poimi esine maasta (collect_item)")
        print("4. Lisää esine manuaalisesti")
        print("5. Katso tilanne ja koordinaatit")
        print("6. Lepää ja palauta energia")
        print("7. Tallenna peli")
        print("8. Poistu kaivoksesta")

        valinta = input("Valitse toiminto (1-9): ").strip()

        match valinta:
            case "1":
                louhi_ja_liiku(pelaaja)
            case "2":
                poimi_esine(pelaaja)
            case "3":
                tulosta_reppu(pelaaja)
            case "4":
                lisaa_oma_muistiinpano(pelaaja)
            case "5":
                tulosta_tiedot(pelaaja)
            case "6":
                lepaa(pelaaja)
            case "7":
                if tarkista_loppuratkaisut(pelaaja):
                    print("\nOnneksi olkoon, läpäisit pelin!")
                    break
            case "8":
                tallenna_peli(pelaaja)
            case "9":
                print("\nLopetit pelin ja poistuit alueelta.")
                break
            case _:
                print("Virheellinen valinta. Valitse numero väliltä 1-9.")


if __name__ == "__main__":
    main()