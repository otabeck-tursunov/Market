toplam = {
    'Matematika': ['Ildiz', 'Daraja'],
    'Futbol': ["To'p", 'Offside'],
    'Parfyumeriya': ['Pamada']
}


class Termin:
    def __init__(self):
        self.d = dict()

    def qoshish(self, soha, termin):
        if soha not in self.d.keys():
            self.d.update({soha: [termin, ]})
        else:
            value = self.d.get(soha)
            value.append(termin)
            self.d.update({soha: value})

    def qidirish(self, termin):
        for key, value in self.d.items():
            if termin in value:
                return key
        return f"{termin} nomli termin mavjud emas!"

    def eng_katta_soha(self):
        eng_katta = None
        for key, value in self.d.items():
            if eng_katta is None or len(self.d.get(eng_katta)) < len(value):
                eng_katta = key
        return eng_katta

    def sohani_top(self, matn: str):
        sohalar = []
        matn = matn.split()
        for soz in matn:
            for soha, terminlar in self.d.items():
                if soz.lower() in terminlar:
                    sohalar.append(soha)
        natija = ""
        for soha in set(sohalar):
            natija += soha + " "
        return f"{natija}sohalari haqida gap bormoqda"


obj1 = Termin()
obj1.qoshish("Matematika", "ildiz")
obj1.qoshish("Matematika", "daraja")
obj1.qoshish("Matematika", "karra")
obj1.qoshish("Futbol", "to'p")
obj1.qoshish("Futbol", "offside")
obj1.qoshish("Futbol", "kartochka")
obj1.qoshish("Parfyumeriya", "pamada")


# print(obj1.d)
# print(obj1.qidirish("Qizil kartochka"))
# print(obj1.eng_katta_soha())
# print(obj1.sohani_top("Bugun o'yinda 2 karra qizil kartochka va 3 karra sariq kartochka olindi"))


class Balans:
    def __init__(self, balance):
        self.kirimlar = []
        self.chiqimlar = []
        self.balance = balance

    def kirim(self, miqdor: int, izoh: str):
        self.kirimlar.append([miqdor, izoh])
        self.balance += miqdor
        return self.balance

    def chiqim(self, miqdor, izoh):
        self.chiqimlar.append([miqdor, izoh])
        self.balance -= miqdor
        return self.balance

    def eng_katta_kirim(self):
        index = 0
        for i in range(len(self.kirimlar)):
            if self.kirimlar[index][0] < self.kirimlar[i][0]:
                index = i
        return f"Miqdor: {self.kirimlar[index][0]} \nIzoh: {self.kirimlar[index][1]}"

    def statistika(self):
        natija = "Kirimlar \n"
        for kirim in self.kirimlar:
            natija += f"{str(kirim[0]).rjust(5, " ")} $: {kirim[1]}\n"

        natija += "\nChiqimlar \n"
        for chiqim in self.chiqimlar:
            natija += f"{str(chiqim[0]).rjust(5, " ")} $: {chiqim[1]}\n"

        return natija


john = Balans(5000)
john.kirim(100, "Musobaqa")
john.kirim(500, "Ish haqi")
john.kirim(100, "Avans")
john.chiqim(10, "Tushlik")
john.chiqim(150, "Kiyim-kechak")
john.chiqim(3000, "Sayohat uchun")

print(john.eng_katta_kirim())
print(john.statistika())
