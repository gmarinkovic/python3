# Одредити колико флаша дате запремине је могуће напунити датом количином лимунаде.
#
# Улаз: Са стандардног улаза учитавају се два позитивна реална броја. У првом реду дата је запремина флаше
# у литрима као позитиван реалан број на до три децимале, а у другом је дата расположива количина лимунаде
# у литрима, такође на до три децимале. Запремина флаше није већа од 5 литара, а колична лимунаде није већа
# од 50 литара.
#
# Излаз: На стандардни излаз исписати цео број који представља број флаша које је могуће напунити.
#
# Пример
# Улаз
# 0.2
# 0.6
# Излаз
# 3

import math

# Ubacili smo npr 10 samo da bi iskocili iznad 1 kako bi prevazisli probleme sa deljenjem floata
v_flase = float(input("Unesi zapreminu flase: "))
v_limunade = float(input("Unesi ukupnu zapreminu limunade za istakanje: "))

broj_flasa = math.floor(1e-6 + v_limunade / v_flase)

print(broj_flasa)
