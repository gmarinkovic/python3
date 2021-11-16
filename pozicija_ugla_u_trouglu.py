# Дата су два угла разностраничног троугла у степенима, минутима и секундама. Одредити који од углова
# троугла је највећи, први по редоследу уноса, други по редоследу уноса или трећи, одређен у програму.
#
# Улаз: У свакој од шест линија стандардног улаза налази се по један цео број. Бројеви редом представљају
# степене, минуте (мање од 60) и секунде (мање од 60), прво једног, па другог угла троугла. Збир дата два угла
# је мањи од 180 степени.
#
# Излаз: У једној линији стандардног излаза исписати број 1, 2 или 3.
#
# Пример
# Улаз
# 75 30 14
# 23 15 45
# Излаз
# 3

a1, a2, a3 = map (int,input("Unesi prvi ugao trougla 'stepeni minuti sekunde' : ").split())
b1, b2, b3 = map (int,input("Unesi drugi ugao trougla 'stepeni minuti sekunde' : ").split())

c  = 180*60*60 - (  (a1+b1)*60*60 + (a2+b2)*60 + (a3+b3)  )
c1 = c // 3600
c2 = (c % 3600) // 60
c3 = (c % 3600) %  60

def ugao_u_sekundama(a,b,c):
    s=a*60*60+ b*60+c
    return s

maks= max(ugao_u_sekundama(a1,a2,a3),ugao_u_sekundama(b1,b2,b3),ugao_u_sekundama(c1,c2,c3))

if (ugao_u_sekundama(a1,a2,a3) == maks): print("1")
if ugao_u_sekundama(b1,b2,b3) == maks:   print("2")
if ugao_u_sekundama(c1,c2,c3) == maks:   print("3")
