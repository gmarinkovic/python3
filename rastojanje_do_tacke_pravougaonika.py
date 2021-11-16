# Деца се играју јурке у школском дворишту правоугаоног облика и око њега. Правила игре су таква да је
# ученик безбедан када се ухвати за ограду. Напиши програм који одређује колико је најмање растојање које
# Ђока треба да претрчи да би био безбедан (он се у почетку може налазити и у дворишту и ван њега).
#
# Улаз: Са стандардног улаза учитава се 6 реалних бројева (сваки у посебном реду):
# • x0, y0 (0 ≤ x0, y0 < 1000) - координате доњег левог темена правоугаоника који представља школско
# двориште у координатном систему постављеном тако да су ивице правоугаоника паралелне координатним осама.
# • x1, y1 (x0 < x1 ≤ 1000, y0 < y1 ≤ 1000) координате горњег десног темена правоугаоника.
# • x, y (0 ≤ x0, y0 ≤ 1000) - координате тачке на којој се налази Ђока.
#
# Излаз: На стандардни излаз исписати један реалан број - најкраће растојање Ђака до ограде у метрима
# (допуштена је толеранција је један центиметар, тј. резултат исписати заокружен на две децимале).
#
# Пример 1
# Улаз
# 100 100
# 200 200
# 50  170
# Излаз
# 50.00
#
# Пример 2
# Улаз
# 100 100
# 200 200
# 50  300
# Излаз
# 111.80
import math

a1, a2 = map(int, input("Unesi koordinate prve tacke pravougaonika: ").split())
b1, b2 = map(int, input("Unesi koordinate druge dijagonalno suprotne tacke pravougaonika: ").split())
c1, c2 = map(int, input("Unesi koordinate tacke lokacije deteta: ").split())

if c1 in range (a1,b1):
    if (c2-a2 > b2-c2 and c2<b2) or (c2>b2):
        print("Najblize rastojanje je ","{:.2f}".format(c2-b2))
    else:
        print("Najblize rastojanje je ", "{:.2f}".format(c2-a2))

if c2 in range (a2,b2):
    if (abs(c1-a1) > b1-c1 and c1<a1) or (c1>b1):
        print("Najblize rastojanje je ","{:.2f}".format(abs(c1-b1)))
    else:
        print("Najblize rastojanje je ", "{:.2f}".format(abs(c1-a1)))

if (c1<a1 or c1>b1) and (c2<a2 or c2>b2):
    rastojanje1 = math.sqrt(pow(c1 - a1,2) + pow(c2 - a2,2))
    rastojanje2 = math.sqrt(pow(c1 - a1,2) + pow(c2 - b2,2))
    rastojanje3 = math.sqrt(pow(c1 - b1,2) + pow(c2 - a2,2))
    rastojanje4 = math.sqrt(pow(c1 - b1,2) + pow(c2 - b2,2))
    print("Najblize rastojanje je ", "{:.2f}".format(min(rastojanje1,rastojanje2,rastojanje3,rastojanje4)))
