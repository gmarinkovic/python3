# Аца је добио n јабука и на једнаке делове (по трећину) поделио браћи Бранку, Цанету, и Душану. Преостале
# јабуке појео је сам. Бранко је своје јабуке поделио браћи (Аци, Цанету и Душану), а што је преостало појео
# је сам. Тако је затим поступио и Цане, а онда и Душан. Колико јабука после овакве поделе има свако од њих
# (занемарујући оне које су поједене).
#
# Улаз: Број јабука n које је добио Аца.
#
# Излаз: Број јабука које на крају има Аца (први ред), Бранко (други ред), Цане (трећи ред) и Душан (четврти
# ред).
#
# Пример
# Улаз
# 100
# Излаз
# 44
# 33
# 19
# 0

def podela(x, y, z, w):
    y1 = y + x // 3 # Osoba x osobama y, z i w
    z1 = z + x // 3 # daje po trecinu svojih jabuka,
    w1 = w + x // 3 # a ono sto ostane pojede sam.
    x1 = 0
    return (x1, y1, z1, w1)
Aca = int(input("Unesi broj jabuka koje ima Aca u startu: "))
Branko = 0
Cane = 0
Dusan = 0
# Aca daje po trecinu Branku, Canetu i Dusanu - ostatak pojede
(Aca, Branko, Cane, Dusan) = podela(Aca, Branko, Cane, Dusan)
# Branko daje po trecinu Aci, Canetu i Dusanu - ostatak pojede
(Branko, Aca, Cane, Dusan) = podela(Branko, Aca, Cane, Dusan)
# Cane daje po trecinu Aci, Branku i Dusanu - ostatak pojede
(Cane, Aca, Branko, Dusan) = podela(Cane, Aca, Branko, Dusan)
# Dusan daje po trecinu Aci, Branku i Canetu - ostatak pojede
(Dusan, Aca, Branko, Cane) = podela(Dusan, Aca, Branko, Cane)
print("Aca ima jabuka: "+str(Aca))
print("Branko ima jabuka: "+str(Branko))
print("Cane ima jabuka: "+str(Cane))
print("Dusan ima jabuka: "+str(Dusan))
