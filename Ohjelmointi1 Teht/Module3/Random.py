import random

#en ole korjaamassa tätä vaikka voisin koska tämä toimii paremmin kun joku muu helpompi tapa#
print("Kolminumeroinen koodi: ")
for _ in range(3):
    print(random.randint(1, 6,), end=" ")

print("\n")

print("Nelinumeroinen koodi: ")
for _ in range(4):
    print(random.randint(0, 9,),end=" ")