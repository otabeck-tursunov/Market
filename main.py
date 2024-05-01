def eng_uzun_ism(*ismlar):
    return max(ismlar, key=len)


# print(eng_uzun_ism("Otabek", "Shukurjon", "Xojiakbar", "Asadbek", "Adhamjon"))


def uzun_ism(toplam: list):
    return max(toplam, key=len)


# ismlar = input("Vergul bilan ism kiriting: ").split(",")
# print(uzun_ism(ismlar))


def qoshish(key, value, dict: dict) -> None:
    dict.update({key: value})


poytaxt = {"uzb": "Toshkent", "uk": "London"}
qoshish("usa", "Vashington", poytaxt)


# print(poytaxt)


def tekshir(son, start, end):
    if son in range(start, end):
        return True
    return False


# print(tekshir(5, 1, 10))


def calculator(son1: float, amal: str, son2: float):
    match amal:
        case "+":
            return f"{son1} + {son2} = {son1 + son2}"
        case "-":
            return f"{son1} - {son2} = {son1 - son2}"
        case "*":
            return f"{son1} * {son2} = {son1 * son2}"
        case "/":
            return f"{son1} / {son2} = {son1 / son2}"


# print(calculator(2, "+", 7))


def qoshish(qiymat, toplam: list):
    toplam.append(qiymat)


sonlar = [1, 2, 3, 4]
qoshish(10, sonlar)


# print(sonlar)


def ochir(toplam: list, indeks=None):
    if indeks is not None:
        toplam.pop(indeks)
    else:
        toplam.pop()


ochir(sonlar)
# print(sonlar)

sonlar2 = [-1, -2, -3]


def biralshtir(list1: list, list2: list):
    list1.extend(list2)


# biralshtir(sonlar, sonlar2)
# print(sonlar)


def uzunlikni_top(son):
    return len(str(son))


# son = int(input("Son kiriting: "))
# print(uzunlikni_top(son))


def tasma(matn: str):
    return matn.strip()


soz = "   Salom  "
print(tasma(soz))
