# Написати програм који за четири дата броја одређује који је од та четри броја најближи
# аритметичкој средини датих бројева (ако су два броја једнако близу исписати први).
#
# Улаз: У четири линије стандардног улаза налазе се четири реална броја.
#
# Излаз: У једној линији стандардног излаза приказати један од унетих реалних бројева, на две децимале,
# најближи њиховој аритметичкој средини.
#
# Пример
# Улаз
# 24.3
# 20.2
# 23.5
# 22.7
# Излаз
# 22.70

a = float(input("Uneti prvi broj: "))
b = float(input("Uneti drugi broj: "))
c = float(input("Uneti treci broj: "))
d = float(input("Uneti peti broj: "))

sredina = (a+b+c+d)/4
minimum= min(abs(sredina-a), min( abs(sredina-b),min(abs(sredina-c),abs(sredina-d))))

print("Najblizi broj proseku je: "+"{:.2f}".format(minimum+sredina))
