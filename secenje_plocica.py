# Правоугаону терасу димензија d×s центиметара квадратних треба поплочати коришћењем плочица квадратног облика
# странице p центиметара, које се постављају тако да су им странице паралелне страницама терасе.
# Написати програм којим се одређује колико се плочица мора сећи ради поплочавања, као и површину дела
# терасе који заузимају сечене плочице. Од сваке сечене плочице користи се један део, а други одбацује.
#
# Улаз:
# • p - страница плочице у cm (10 ≤ p ≤ 50)
# • d - дужина просторије у cm (200 ≤ d ≤ 10000)
# • s - ширина просторије у cm (200 ≤ s ≤ 10000)
#
# Излаз: Број плочица које се морају сећи и површина коју покривају сечене плочице.
#
# Пример
# Улаз
# 20
# 310
# 270
# Излаз
# 29
# 5700

p = int(input("Unesi dimenziju stranice plocice u cm: "))
d = int(input("Unesi duzinu prostorije: "))
s = int(input("Unesi sirinu prostorije: "))

dfloor = d // p                 # celobrojni broj celih plocica po duzini
dceil = (d + p - 1) // p        # broj plocica, zajedno sa onom koja ce se se seci, po duzini

sfloor = s // p                 # celobrojni broj celih plocica po sirini
sceil = (s + p - 1) // p        # broj plocica, zajedno sa onom koja ce se se seci, po sirini

# dceil*sceil - minimalni broj plocica koje pokrivaju oblast
# dfloor*sfloor - maksimalni broj plocica koje su sadrzane u oblasti

print()

broj_secenih_plocica = (dceil * sceil) - (dfloor * sfloor)
povrsina_pokrivena_secenim_plocicama = (d*s) - (dfloor*p*sfloor*p)

print("Broj secenih plocica: ",broj_secenih_plocica)
print("Povrsina pokrivena secenim plocicama",povrsina_pokrivena_secenim_plocicama)
