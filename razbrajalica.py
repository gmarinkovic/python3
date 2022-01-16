# Деца стоје у кругу и одређују ко ће од њих да жмури тако што изговарају неку разбрајалицу (на пример, еципеци-пец).
# Ако децу обележимо бројевима од 0 до n − 1, редом како стоје у кругу, ако је познат број речи
# (слогова) разбрајалице и ако је познат редни број детета од којег почиње разбрајање, напиши програм који
# приказује редни број детета које је одабрано да жмури (тј. на коме се разбрајање завршава).
#
# Улаз: Уносе се три природна броја. Број слогова разбрајалице, број деце и редни број детета од којег почиње
# разбрајање. Претпоставићемо да је број деце мањи од 100, а да је број слогова мањи од 1000.
#
# Излаз: Исписује се један природни број – редни број детета одабраног да жмури.
# Пример
# Улаз
# 13
# 7
# 3
# Излаз
# 1

broj_slogova = int(input("Unesi broj slogova razbrajalice: "))
broj_dece = int(input("Unesi broj  dece: "))
redni_broj_prvog_deteta = int(input( "Unesi redni broj prvog deteta: "))

print((redni_broj_prvog_deteta +broj_slogova) % broj_dece-1 )