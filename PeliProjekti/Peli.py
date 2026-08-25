nimi = input("Mikä sinun nimesi on: ")
ikä = int(input("Kuinka vanha olet: "))


while True:
    if ikä < 12:
        print("Olet ala ikäinen.")
        break
    else:
        print(f"Sinun nimesi on: {nimi} ja olet {ikä}")
        break
