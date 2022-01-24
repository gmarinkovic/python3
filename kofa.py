# У дечијем базену постоји гусарски брод на чијем се врху налази кофа која се празни на сваких k минута. Ако
# се зна број минута протеклих од неког ранијег пражњења кофе напиши програм који одређује број минута
# преосталих до првог следећег минута у коме ће се кофа сигурно испразнити (0 ако ће се кофа испразнити у
# тренутном минуту).
#
# Улаз: У првом реду стандардног улаза налази се цео позитиван број k (0 < k ≤ 60) који представља број
# минута између свака два узастопна пражњења кофе, а у другом број n (0 ≤ n ≤ 240) који представља број
# минута од неког претходног пражњења кофе.
#
# Излаз: На стандардни излаз исписати тражени број.
#
# Пример 1
# Улаз
# 5
# 23
# Излаз
# 2
# Пример 2
# Улаз
# 5
# 25
# Излаз
# 0


k = int(input("Unesi broj minuta za koji se isprazni kanta: "))
n = int(input("Unesi broj minuta do neke naredne provere: "))

print((n+ k -1)//k * k - n) if n%k != 0 else print(0)
