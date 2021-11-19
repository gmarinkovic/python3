# (bez nizova,lista, mapa,...)
# 
# Три аутомобила крећу са стартне позиције у тренуцима 0 ≤ t1 ≤ t2 ≤ t3 константним брзинама v1, v2 и
# v3. Приказати стартне бројеве аутомобила који су на водећој позицији у тренутку t (t ≥ 0). Ако ни један
# аутомобил још није кренуо, сва три су у водећој позицији.
#
# Улаз: Са стандардног улаза учитава се седам целих бројева, сваки у засебној линији t1, v1, t2, v2, t3, v3, t где
# t1, t2, t3, t представљају времена у секундама, а v1, v2, v3 брзине у метрима по секунди.
#
# Излаз: На стандардни излаз исписати један или више целих бројева (сваки у посебном реду)
# који представљају редне бројеве аутомобила (1, 2 или 3) који су на водећој позицији.
# Ако је више аутомобила истовремено у вођству, њихове редне бројеве исписати у растућем редоследу.

# Пример
# Улаз
# 10
# 5
# 5
# 4
# 0
# 2
# 30
# Излаз
# 1
# 2

t1 = int(input("Unesi vreme prvog vozila: "))
v1 = int(input("Unesi brzinu prvog vozila: "))
t2 = int(input("Unesi vreme drugog vozila: "))
v2 = int(input("Unesi brzinu drugog vozila: "))
t3 = int(input("Unesi vreme treceg vozila: "))
v3 = int(input("Unesi brzinu treceg vozila: "))

t = int(input("Unesi kontrolno vreme: "))

def vreme(t, tx):
    if t <= tx:
        return t
    else:
        return tx

poz1 = v1 * vreme(t, t1)
k3 = 3

if v2 * vreme(t, t2) > poz1:
    poz2 = poz1
    poz1 = v2 * vreme(t, t2)
    k1 = 2
    k2 = 1
else:
    poz2 = v2 * vreme(t, t2)
    k1 = 1
    k2 = 2

if v3 * vreme(t, t3) > poz1:
    poz2 = poz1
    poz1 = v3 * vreme(t, t3)
    k3 = k2
    k2 = k1
    k1 = 3
elif v3 * vreme(t, t3) > v2 * vreme(t, t2):
    k3 = k2
    k2 = 3
else:
    k3 = 3

print(k1)
print(k2)
print(k3)
