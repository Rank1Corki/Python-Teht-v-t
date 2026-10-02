import os
from models.room import Room
from models.player import Player
from models.item import Item

# Määritetään tallennuspolut suoraan täällä, jotta import main -kehäviittausta ei tarvita
PROJEKTI_KANSIO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_KANSIO = os.path.join(PROJEKTI_KANSIO, "data")
TALLENNUS_POLKU = os.path.join(DATA_KANSIO, "savegame.txt")


class Save:
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
                f.write(
                    f"{pelaaja.name};{pelaaja.age};{pelaaja.energia};"
                    f"{pelaaja.x};{pelaaja.y};{pelaaja.syvyys};{pelaaja.location.name}\n"
                )
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

    def poista_tallennus_pelin_paattyessa():
        """Poistaa savegame-tiedoston, jotta voitettu peli ei jatku vanhasta tilasta."""
        if os.path.exists(TALLENNUS_POLKU):
            try:
                os.remove(TALLENNUS_POLKU)
            except OSError:
                pass