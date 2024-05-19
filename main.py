sudoku = """
  --- --- --- ---
 | a | b | c | d |
  --- --- --- ---
 | e | f | g | h |
  --- --- --- ---
 | j | k | l | m |
  --- --- --- ---
 | n | o | p | q |
  --- --- --- ---

"""
harflar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q']
sonlar = []
h1 = []
h2 = []
h3 = []
h4 = []
h5 = []
h6 = []
h7 = []
h8 = []
h9 = []
h10 = []
h11 = []
h12 = []

import random

b = random.randint(1, 4)
h1.append(b)
h5.append(b)
h10.append(b)
harflar.remove('b')
sudoku = sudoku.replace("b", str(b))
g = random.randint(1, 4)
h2.append(g)
h6.append(g)
h11.append(g)
harflar.remove('g')
sudoku = sudoku.replace("g", str(g))
m = random.randint(1, 4)
h4.append(m)
h7.append(m)
h12.append(m)
harflar.remove('m')
sudoku = sudoku.replace("m", str(m))
n = random.randint(1, 4)
h3.append(n)
h8.append(n)
h9.append(n)
harflar.remove('n')
sudoku = sudoku.replace("n", str(n))
print(sudoku)
qadam = 0
while qadam < 9:
    harf = input("qaysi harf o'rniga son qo'ymoqchisiz ")
    while harf not in harflar:
        print("iltimos bizda mavjud harfnikiriting va u avval kiritilmagan bo'lsin")
        harf = input("qaysi harf o'rniga son qo'ymoqchisiz ")
    harflar.remove(harf)
    son = int(input("xo'sh qaysi sonni qo'yasiz faqat 1-4 orliqda bo'lsin"))
    while son not in range(1, 5):
        son = int(input("iltimos 1-4 oraliqda bo'lsin 1-4 orliqda bo'lsin"))
    sudoku = sudoku.replace(harf, str(son))
    print(sudoku)
    qadam += 1
    if qadam == 8:
        print("tabriklayman siz galaba qozondiz")
    if harf == 'a':
        h1.append(son)
        h5.append(son)
        h9.append(son)
    if harf == 'c':
        h2.append(son)
        h5.append(son)
        h11.append(son)
    if harf == 'd':
        h2.append(son)
        h5.append(son)
        h12.append(son)
    if harf == 'e':
        h1.append(son)
        h6.append(son)
        h9.append(son)
    if harf == 'f':
        h1.append(son)
        h6.append(son)
        h10.append(son)
    if harf == 'h':
        h2.append(son)
        h6.append(son)
        h12.append(son)
    if harf == 'j':
        h3.append(son)
        h7.append(son)
        h9.append(son)
    if harf == 'k':
        h3.append(son)
        h7.append(son)
        h10.append(son)
    if harf == 'l':
        h4.append(son)
        h7.append(son)
        h11.append(son)
    if harf == 'o':
        h3.append(son)
        h8.append(son)
        h10.append(son)
    if harf == 'p':
        h4.append(son)
        h8.append(son)
        h11.append(son)
    if harf == 'q':
        h4.append(son)
        h8.append(son)
        h12.append(son)
    if h1.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h1.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h1.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h1.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h2.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h2.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h2.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h2.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h3.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h3.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h3.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h3.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h4.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h4.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h4.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h4.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h5.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h5.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h5.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h5.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h6.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h6.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h6.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h6.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h7.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h7.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h7.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h7.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h8.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h9.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h9.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h9.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h9.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h10.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h10.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h10.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h10.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h11.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h11.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h11.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h11.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h12.count(1) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h12.count(2) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h12.count(3) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
    if h12.count(4) == 2:
        print("sizni tabriklay olmayman chunki siz yutqizdiz")
        break
