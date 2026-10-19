kuhaalimitta = int(42)

while True:
    try:
        kuhakoko = int(input("Minkä kokoinen kuhasi on: "))
    except ValueError:
        print("invalid input")
        continue
    
    jaljella = kuhaalimitta - kuhakoko

    if kuhakoko >= kuhaalimitta:
        print("Hieno kuha ja sitten kidukset auki ja jäille.")
        break
    else:
        print(f"Kuha on {jaljella} cm liian lyhyt. Heitä kuha takaisin veteen!")
        