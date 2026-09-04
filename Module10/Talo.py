class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.kerros = alin_kerros


    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros += 1
        print(f"Hissi on nyt {self.kerros} kerroksessa.")

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
        print(f"Hissi on nyt {self.kerros} kerroksessa.")


class Talo:
    def __init__(self,alin_kerros, ylin_kerros, hissien_lkm=5):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.hissit = []
        for _ in range(hissien_lkm):
            self.hissit.append(Hissi(self.alin, self.ylin))



    def aja_hissiä(self, hissin_numero, kohdekerros):
        if kohdekerros < self.alin or kohdekerros > self.ylin:
            print(f"Kerros {kohdekerros} ei ole olemassa.")
            return

        valittu_hissi = self.hissit[hissin_numero - 1]
        while valittu_hissi.kerros < kohdekerros:
            valittu_hissi.kerros_ylos()

        while valittu_hissi.kerros > kohdekerros:
            valittu_hissi.kerros_alas()


    def palohälytys(self):
        for i in range(len(self.hissit)):
            hissin_nmr = i + 1 
            self.aja_hissiä(hissin_nmr, self.alin)


if __name__ == "__main__":
    talo = Talo(1, 10, 4)
    talo.aja_hissiä(1, 5)

    print("Palohälytys.")
    talo.palohälytys()
    print(f"Hissi on nyt alimmassa kerroksessa")
    talo.aja_hissiä(1, 5)

