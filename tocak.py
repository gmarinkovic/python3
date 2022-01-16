# Напиши програм који на основу пречника точка бицикла, брзине кретања бицикла и времена које се бицикл
# креће одређује колико пута се точак окренуо (рачунајући и окрет који још није потпуно завршен).
#
# Улаз: Са стандардног улаза се учитавају реални бројеви који представљају пречник точка бицикла у cm,
# брзину кретања бицикла у m/s и време кретања бицикла у s.
# Подаци су такви да точак није довршио последњи окрет који је започео.
#
# Излаз: На стандардни излаз се записује један цео број који представља број започетих окрета бицикла.
#
# Пример
# Улаз
# 60
# 5
# 5
# Излаз
# 14

import math

precnik_tocka_u_cm = float(input("Unesi precnik tocka u cm: "))
brzina_bicikla_u_m_s = float(input("Unesi brzinu bicikla u metrima po sekundi: "))
vreme_u_s = float(input("Unesi vreme okretanja tocka tj voznje bicikla: "))

obim_tocka_u_m = (precnik_tocka_u_cm / 100.0) * math.pi
predjeni_put_u_m = brzina_bicikla_u_m_s * vreme_u_s
broj_zapocetih_krugova = math.ceil(predjeni_put_u_m / obim_tocka_u_m)

print("Broj Zapocetih krugova je: ",broj_zapocetih_krugova)
