# RAD SA VREMENIMA i njihovim pozicionim zapisima

#Два тркача трче по кружној стази дужине s km, један брзином од v1 km/h, други брзином од v2 km/h.
# Колико ће времена требати бржем тркачу да за цео круг престигне споријег?
#
# Улаз: Подаци на две децимале:
# • s - дужина кружне стазе (1 ≤ s ≤ 10)
# • v1 - брзина првог тркача (1 ≤ v1 ≤ 45)
# • v2 - брзина другог тркача (1 ≤ v2 ≤ 45)
#
# Излаз: Целобројне вредности броја сати, минута и секунди, које представљају време потребно да спорији
# тркач за цео круг сустигне споријег. Секунде приказати заокружене на најближу целобројну вредност.
#
# Пример
# Улаз
# 10.00
# 5.00
# 6.00
#
# Излаз
# 10
# 0
# 0
def u_sat_min_sek(sekunde):
    sekunde_konacne=sekunde%60
    minute= (sekunde//60)%60
    sati= sekunde//3600
    return (sati,minute, sekunde_konacne)

s= int(input("Unesi duzinu kruzne staze u kilometrima (do 10 km): "))
v1= int(input("Unesi brzinu prvog trkaca u km/h (raspon 1-45) : "))
v2= int(input("Unesi brzinu drugog trkaca u km/h (raspon 1-45) : "))

t= int((s*1000)/(abs(v1-v2)*1000/3600))

(h,m,s)=u_sat_min_sek(t)

print(h)
print(m)
print(s)
