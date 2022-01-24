# Животиње у зоолошком врту воле да једу воће. У врт се допремају пакети воћа у којима се налази a килограма
# ананаса, b килограма банана и j килограма јабука. Волонтери треба да припреме дневни оброк за који знају
# да треба да садржи бар A килограма ананаса, B килограма банана и J килограма јабука. Напиши програм
# који израчунава који је најмањи број пакета воћа које волонтери треба да наруче да би могли да припреме
# дневни оброк.
#
# Улаз: Са станардног улаза учитава се 6 целих бројева, сваки у посебном реду: a, b, j, из интервала [1, 5] и A,
# B, J из интервала [5, 100].
#
# Излаз: На стандардни излаз исписати један цео број који представља број пакета које треба наручити.
#
# Пример
# Улаз
# 3
# 5
# 4
# 12
# 14
# 17
# Излаз
# 5
import math

print("Paket voca sadrzi:")
a = int(input("Unesi kolicinu banana: "))
b = int(input("Unesi kolicinu ananasa: "))
j = int(input("Unesi kolicinu jabuka: "))

print()
print("Potraznja zoloskog vrta je za vocem:")
A = int(input("Unesi kolicinu banana: "))
B = int(input("Unesi kolicinu ananasa: "))
J = int(input("Unesi kolicinu jabuka: "))

print(max(math.ceil(A/a),math.ceil(B/b),math.ceil(J/j)))
