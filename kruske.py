# Учитељица је купила k крушака, које жели да подели ученицима из свог одељења. Ако у одељењу има u
# ученика, колико још најмање крушака учитељица треба да купи да би била сигурна да ће сваком детету моћи
# да да исти број крушака.
# Улаз: Са стандардног улаза уносе се два природна броја (сваки у посебном реду):
# • k (0 ≤ k ≤ 300) број крушака које учитељица тренутно има.
# • u број ученика у одељењу (15 ≤ u ≤ 30).
# Излаз: На стандардни излаз исписати један цео број који представља најмањи број крушака које учитељица
# треба да купи.
# Пример 1
# Улаз
# 73
# 23
# Излаз
# 19
# Пример 2
# Улаз
# 100
# 20
# Излаз
# 0

krusaka = int(input("Unesi broj krusaka koje je kupila uciteljica: "))
ucenika = int(input("Unesi broj ucenika: "))

krusaka_po_uceniku = (krusaka + ucenika - 1) // ucenika
ukupno_krusaka = krusaka_po_uceniku * ucenika
nedostaje = ukupno_krusaka - krusaka
print("Najmanji broj krusaka koje treba da se dokupe: ",nedostaje)
