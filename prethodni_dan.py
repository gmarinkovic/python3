# Напиши програм који за унети датум одређује датум претходног дана.
#
# Улаз: Са стандардног улаза се уносе три позитивна цела броја (сваки у засебном реду) која представљају дан,
# месец и годину једног исправног датума.
#
# Излаз: На стандардни излаз исписати три цела броја која представљају дан, месец и годину јучерашњег
# датума. Сви бројеви се исписују у једном реду, а иза сваког броја наводи се тачка.
#
# Пример 1
# Улаз
# 1
# 3
# 2016
# Излаз
# 29
# 2
# 2016
#
# Пример 2
# Улаз
# 1
# 3
# 1900
# Излаз
# 28.2.1900.
#
# Пример 3
# Улаз
# 1
# 1
# 2014
# Излаз
# 31.12.2013.

# provera da li je data godina prestupna
def prestupna(godina):
    return (godina % 4 == 0 and godina % 100 != 0) or (godina % 400) == 0

# broj dana u datom mesecu date godine
def broj_dana_u_mesecu(mesec, godina):
    if mesec in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif mesec in {4, 6, 9, 11}:
        return 30
    else:
        return 29 if prestupna(godina) else 28

# ucitavamo danasnji datum
dan_danas = int(input("Unesi dan u mesecu (1-31): "))
mesec_danas = int(input("Unesi mesec u godini (1-12): "))
godina_danas = int(input("Unesi godinu: "))

# izracunavamo sutrasnji datum
if dan_danas - 1 >= 1:

#   prethodni dan pripada tekucem mesecu
    prethodni_dan = dan_danas - 1
    prethodni_mesec = mesec_danas
    prethodna_godina = godina_danas
else:
#       danas je prvi dan u mesecu
    if mesec_danas - 1 >= 1:
#       prelazimo na prvi dan narednog meseca
        prethodni_dan = broj_dana_u_mesecu(mesec_danas - 1, godina_danas)
        prethodni_mesec = mesec_danas - 1
        prethodna_godina = godina_danas
    else:
#       danas je prvi dan u prvom mesecu (01.01.)
        prethodni_dan = 31
        prethodni_mesec = 12
        prethodna_godina = godina_danas - 1
        
#       ispisujemo prethodni datum
print(str(prethodni_dan)+"."+str(prethodni_mesec)+"."+str(prethodna_godina))
#print(prethodni_dan,".",prethodni_mesec,".",prethodna_godina,sep="")
