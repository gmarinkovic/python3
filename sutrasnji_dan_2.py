# Напиши програм који за унети датум одређује датум наредног дана.
# Улаз: Са стандардног улаза се уносе три позитивна цела броја (сваки у засебном реду) која представљају дан,
# месец и годину једног исправног датума.
# Излаз: На стандардни излаз исписати три цела броја која представљају дан, месец и годину сутрашњег датума. Сви бројеви се исписују у једном реду, а иза сваког броја наводи се тачка.
#
# Пример 1
# Улаз
# 1
# 1
# 2016
# Излаз
# 2.1.2016.
#
# Пример 2
# Улаз
# 28
# 2
# 2016
# Излаз
# 29.2.2016.
#
# Пример 3
# Улаз
# 28
# 2
# 1900
# Излаз
# 1.3.1900.
#
# Пример 4
# Улаз
# 31
# 12
# 2017
# Излаз
# 1.1.2018.

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

# ucitavamo datum
dan = int(input("Unesi dan u mesecu (1-31): ")); 
mesec = int(input("Unesi mesec u godini (1-12): "));
godina = int(input("Unesi godinu: "))

# uvecavamo dan za jedan
dan = dan + 1

if dan > broj_dana_u_mesecu(mesec, godina):
