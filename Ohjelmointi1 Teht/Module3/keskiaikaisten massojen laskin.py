luoti = 13.3
lieviskä = luoti * 20
naula = luoti * 32

luoti1 = float(input("Kuinka monta luotia: "))
naula1 = float(input("Kuinka monta naulaa: "))
lieviskä1 = float(input("Kuinka monta lieviskää: "))

total_grams = (luoti1 * luoti) + (naula1 * naula) + (lieviskä1 * lieviskä)

# Erotetaan kilot (kokonaisluku) ja jäljelle jäävät grammat
kg = int(total_grams // 1000)
grams = int(total_grams % 1000)

# Tulostetaan lopputulos
print(f"{kg} kg and {grams} grams")