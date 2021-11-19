# Три аутомобила стартних бројева 1, 2, 3 крећу са исте стартне позиције редом у тренуцима t1, t2, t3
# (0 ≤ t1 < t2 < t3), и крећу се константним брзинама v1, v2, v3. Написати програм којим одређујемо тренутак кад се
# деси последње претицање, или ако нема претицања исписати текст nema.
#
# Улаз: Са стандардног улаза учитава се 6 реалних бројева. Прва линија садржи бројеве t1, v1, друга бројеве
# t2, v2, а трећа бројеве t3, v3.
#
# Излаз: На стандардни излаз исписати један реалан број који представља време последњег претицања,
# заокружен на две децимале или текст nema ако претицања није било.
#
# Пример 1
# Улаз
# 1.6 20
# 2 12
# 7.4 2.1
# Излаз
# nema
#
# Пример 2
# Улаз
# 6.3 9
# 15 18
# 19 13
# Излаз
# 47.57

t1,v1 = map (float,input("Unesi vreme polaska i brzinu prvog vozila: ").split())
t2,v2 = map (float,input("Unesi vreme polaska i brzinu drugog vozila: ").split())
t3,v3 = map (float,input("Unesi vreme polaska i brzinu treceg vozila: ").split())

# da li je pronađeno jedno preticanje
bilo_preticanja = False

# vreme poslednjeg preticanja
t_poslednjeg_preticanja = 0

# proveravamo da li drugi automobil može preteći prvi
if v2 > v1:
    t_preticanja = (v2*t2 - v1*t1) / (v2 - v1)
    if not bilo_preticanja or t_preticanja > t_poslednjeg_preticanja:
        t_poslednjeg_preticanja = t_preticanja
        bilo_preticanja = True

# proveravamo da li treći automobil moze preteći prvi
if v3 > v1:
    t_preticanja = (v3*t3 - v1*t1) / (v3 - v1)
    if not bilo_preticanja or t_preticanja > t_poslednjeg_preticanja:
        t_poslednjeg_preticanja = t_preticanja
        bilo_preticanja = True

# proveravamo da li treći automobil moze preteći drugi
if v3 > v2:
    t_preticanja = (v3*t3 - v2*t2) / (v3 - v2)
    if not bilo_preticanja or t_preticanja > t_poslednjeg_preticanja:
        t_poslednjeg_preticanja = t_preticanja
        bilo_preticanja = True

# ako je bilo preticanja, prijavljujemo vreme poslednjeg preticanja
if bilo_preticanja:
    print(format(t_poslednjeg_preticanja, '.2f'))
else:
    print("nema")
