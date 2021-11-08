# У соби постоје плава и жута сијалица. За сваку сијалицу је познато време (у облику сат, минут, секунд) када
# је укључена и када је искључена. Напиши програм који одређује колико времена је соба била осветљена
# плаво, колико времена је била осветљена зелено и колико времена је била осветљена жуто (соба је осветљена
# зелено док су истовремено укључене плава и жута сијалица).
#
# Улаз: Са стандардног улаза се уносе четири реда са по три броја раздвојена размацима (сат, минут и секунд
# укључивања плаве сијалица, сат, минут и секунд њеног искључивања, сат, минут и секунд укључивања жуте
# сијалице и сат, минут и секунд њеног искључивања).
#
# Излаз: У првој линији стандардног излаза исписати три броја раздвојена двотачкама која представљају
# време (у сатима, минутима и секундама) које је соба била обојена плаво, у наредној линији у истом облику
# исписати време које је соба била обојена зелено и у последњој линији у истом облику исписати време које је
# соба била обојена жуто.
#
# Пример 1
# Улаз
# 13 15 0
# 14 20 0
# 13 45 0
# 15 30 0
#
# Излаз
# 0:30:0
# 0:35:0
# 1:10:0
#
# Пример 2
# Улаз
# 10 50 20
# 12 40 11
# 8 45 30
# 10 30 20
#
# Излаз
# 1:49:51
# 0:0:0
# 1:44:50

def vreme(h,m,s):
    return h*60*60+m*60+s

def trajanje(s):
    hh = s//3600
    mm = (s//60)%60
    ss = s%60
    return hh,mm,ss

h1, m1, s1 = map(int,input("Unesi pocetak paljenja plava sijalice: ").split())
h2, m2, s2 = map(int,input("Unesi vreme gasenja plava sijalice: ").split())

h3, m3, s3 = map(int,input("Unesi pocetak paljenja zuta sijalice: ").split())
h4, m4, s4 = map(int,input("Unesi vreme gasenja zuta sijalice: ").split())

if (vreme(h3,m3,s3)> vreme(h2,m2,s2) or vreme(h4,m4,s4)<vreme(h1,m1,s1)) :
    hp,mp,sp    = trajanje( vreme(h2,m2,s2) - vreme(h1,m1,s1) )
    hze,mze,sze = trajanje(0)
    hz,mz,sz    = trajanje( vreme(h4,m4,s4) - vreme(h3,m3,s3))

elif vreme(h3,m3,s3)<vreme(h1,m1,s1) and vreme(h4,m4,s4)>vreme(h2,m2,s2) :
    hp,mp,sp    = trajanje(0)
    hze,mze,sze = trajanje(vreme(h2,m2,s2)-vreme(h1,m1,s1))
    hz,mz,sz    = trajanje(vreme(h4,m4,s4)-vreme(h3,m3,s3) - zeleno)

elif vreme(h1,m1,s1) < vreme(h3,m3,s3) and vreme(h2,m2,s2) > vreme(h4,m4,s4) :
    hze,mze,sze = trajanje(vreme(h4,m4,s4) - vreme(h3,m3,s3))
    hp,mp,sp    = trajanje(vreme(h2,m2,s2) - vreme(h1,m1,s1))- zeleno
    hz,mz,sz    = trajanje(vreme(0))

elif vreme(h1,m1,s1) < vreme(h3,m3,s3):
    hp,mp,sp    = trajanje(vreme(h3,m3,s3)- vreme(h1,m1,s1))
    hz,mz,sz    = trajanje(vreme(h4,m4,s4)-vreme(h2,m2,s2))
    hze,mze,sze = trajanje(vreme(h2,m2,s2)-vreme(h3,m3,s3))
else:
    hz,mz,sz    = trajanje(vreme(h1,m1,s1)-vreme(h3,m3,s3))
    hze,mze,sze = trajanje(vreme(h4,m4,s4)-vreme( h1,m1,s1))
    hp,mp,sp    = trajanje(vreme(h2,m2,s2)-vreme(h4,m4,s4))

print("Soba je sijala plavo " +str(hp)+":"+str(mp)+":"+str(sp))
print("Soba je sijala zeleno "+str(hze)+":"+str(mze)+":"+str(sze))
print("Soba je sijala zuto "  +str(hz)+":"+str(mz)+":"+str(sz))
