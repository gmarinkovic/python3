# Четири сумо рвача познатих тежина чекају испред лифта познате носивости. Колики је најмањи број вожњи
# потребан да би се они превезли?
#
# Улаз: Са стандардног улаза учитава се 5 целих бројева, сваки у посебном реду:
# • a, b, c, d (100 ≤ a, b, c, d, ≤ 200) - тежине, у килограмима, 4 сумо рвача,
# • L (200 ≤ L ≤ 700) - носивост лифта у килограмима.
#
# Излаз: На стандардни излаз исписати један цео број - број вожњи потребних да се рвачи превезу.
#
# Пример
# Улаз
# 200
# 103
# 160
# 154
# 280
# Излаз
# 3

# tezine 4 sumo rvaca
a = int(input("Uneti masu prvog sumo rvaca: "))
b = int(input("Uneti masu drugog sumo rvaca: "))
c = int(input("Uneti masu treceg sumo rvaca: "))
d = int(input("Uneti masu cetvrtog sumo rvaca: "))

# nosivost lifta
L = int(input("Uneti dozovoljenu masu za prevoz lifta: "))

# izracunavamo broj voznji
if a+b+c+d <= L:
    broj_voznji = 1
elif ((a+b <= L and c+d <= L) or
    (a+c <= L and b+d <= L) or
    (a+d <= L and b+c <= L) or
    a+b+c <= L or a+b+d <= L or a+c+d <= L or b+c+d <= L):
    broj_voznji = 2
elif (a+b <= L or a+c <= L or a+d <= L or
    b+c <= L or b+d <= L or c+d <= L):
    broj_voznji = 3
else:
    broj_voznji = 4

# ispisujemo rezultat
print("Broj voznji je : "+str(broj_voznji))
