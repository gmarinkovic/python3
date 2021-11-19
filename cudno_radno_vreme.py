# Паја има обичај да да у сред дана напусти радно место и оде негде на кратко. Због тога је објавио необично
# радно време, које се састоји од 4 интервала, са три паузе (четворократно радно време). Напиши програм
# који проверава да ли Паја ради у тренутку t. Сматра се да сваки од ових интервала садржи свој почетак, а не
# садржи свој крај.
#
# Улаз: На стандардном улазу у прва четири реда је задат по један интервал Пајиног радног времена. Сваки
# интервал је задат сатом и минутом почетка и сатом и минутом краја (цели бројеви s1, m1, s2, m2 раздвојени
# размаком, 0 ≤ si ≤ 23, 0 ≤ mi ≤ 59, за i ∈ {1, 2}). Интервали су дисјунктни и поређани хронолошки. У
# петом реду стандардног улаза налазе се цели бројеви S, M раздвојени зарезом, 0 ≤ S ≤ 23, 0 ≤ M ≤ 59,
# који представљају тренутак t, за који се проверава да ли је у Пајином радном времену.
#
# Излаз: На стандардни излаз написати da ако је t у Пајином радном времену тј. ne у супротном.
#
# Пример 1
# Улаз
# 9 0 11 30
# 12 15 14 45
# 15 0 17 0
# 17 15 19 0
# 14 45
# Излаз
# ne

# ucitavanje vremena (sat i minut u istoj liniji, razdvojeni razmakom)
def ucitaj_vreme():
    s, m = input().split()
    return int(s) * 60 + int(m)

# ucitavanje vremenskog intervala (sat i minut pocetka, pa sat i minut kraja,
# sva 4 broja u istoj liniji, razdvojeni razmakom)
def ucitaj_interval():
    s1, m1, s2, m2 = input().split()
    x=int(s1) * 60 + int(m1)
    y=int(s2) * 60 + int(m2)
    return x,y

# ucitavamo intervale radnog vremena i odma preracunava u minute od pocetka dana
a1, b1 = ucitaj_interval()
a2, b2 = ucitaj_interval()
a3, b3 = ucitaj_interval()
a4, b4 = ucitaj_interval()

# ucitavamo trenutak dolaska
t = ucitaj_vreme()

# proveravamo da li je dolazak u nekom od intervala radnog vremena
otvoreno = 0
if a1 <= t and t < b1:
    otvoreno = 1
if a2 <= t and t < b2:
    otvoreno = 1
if a3 <= t and t < b3:
    otvoreno = 1
if a4 <= t and t < b4:
    otvoreno = 1

if otvoreno:
    print("da")
else:
    print("ne")
