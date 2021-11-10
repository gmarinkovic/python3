# Напиши програм који на основу дужина страница троугла проверава да ли такав троугао постоји и да ли је
# једнакостранични, једнакокраки или разностранични.
#
# Улаз: Стандардни улаз садржи три природна броја a, b и c, сваки у посебном реду.
#
# Излаз: На стандардни излаз исписати trougao ne postoji ако не постоји троугао чије су дужине страница
# a, b и c, односно jednakostranicni, jednakokraki или raznostranicni, ако су ти бројеви дужине страница
# одговарајућег троугла.
#
# Пример 1
# Улаз
# 3
# 4
# 5
# Излаз
# raznostranicni
#
# Пример 2
# Улаз
# 3
# 4
# 3
# Излаз
# jednakokraki
#
# Пример 3
# Улаз
# 1
# 5
# 1
# Излаз
# trougao ne postoji

x=int(input("Uesi prvu stranicu trougla: "))
y=int(input("Uesi drugu stranicu trougla: "))
z=int(input("Uesi trecu stranicu trougla: "))

if (x<y+z and y<x+z and z<x+y):
    if x==y==z :
        print("Jednakostranican trougao")
    elif x==y or x==z or y==z:
        print("ravnokraki trougao")
    else:
        print("Raznostrnicni")
else:
    print("Trougao ne postoji")
