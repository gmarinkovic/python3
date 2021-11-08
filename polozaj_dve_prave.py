# Дате су две праве својим имплицитним једначинама (једначинама облика Ax + By + C = 0). Одредити
# њихов међусобни положај (поклапају се, паралелне су или се секу у тачки…)
#
# Улаз: У 6 линија стандардног улаза налази се у свакој по један реалан број. Прва три броја редом представљају коефицијенте A, B и C једне праве, а друга 3 коефицијенте друге праве.
#
# Излаз: У једној линији стандардног излаза исписује се текст poklapaju se за праве које се поклапају,
# paralelne su за паралелне праве или seku se за праве које се секу. Ако се праве секу у другој линији
# стандардног излаза исписују се координате пресечне тачке (2 реална броја са две децимале).
#
# Пример
# Улаз
# 5
# 0
# -10
# 1
# 1
# 0
# Излаз
# seku se
# 2.00 -2.00
print ("Prava je definisana jednacinom Ax + By + C = 0 ")
(a1,b1,c1)= map (int, input("Unesi redom parametre prve prave A b C : ").split())
(a2,b2,c2)= map (int, input("Unesi redom parametre druge prave A b C : ").split())

print(" y=(-A/B)x + (-C/B) ")
if b1 != 0 :
    k1=-a1/b1
    n1=-c1/b1
else:
    k1=0
    n1=0

if b2 != 0 :
    k2=-a2/b2
    n2=-c2/b2
else:
    k2=0
    n2=0

if( k1==k2):
    if(n1==n2):
        print("Prave se poklapaju")
    else:
        print("Prave su paralelne")
else:
    print("Prave se seku")
