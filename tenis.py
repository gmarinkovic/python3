# Напиши програм који на основу броја освојених гемова два играча одређује исход сета у тенису (сет није
# последњи и при резултату 6:6 се игра тај-брејк).
#
# Улаз: Са стандардног улаза се уносе два природна броја (раздвојена размаком) који представљају
# број освојених гемова сваког играча редом.
#
# Излаз: Ако је први играч освојио сет на стандардни излаз исписати поруку pobedio prvi teniser. Ако је други
# играч освојио сет исписати pobedio drugi teniser. Ако унети резултат неисправан исписати neispravno. Ако сет
# још није завршен исписати nije zavrsen set.
#
# Пример 1
# Улаз
# 7 5
# Излаз
# Pobedio prvi teniser
#
# Пример 2
# Улаз
# 3 7
# Излаз
# Neispravno

x,y = map(int,input("Unesi gezultat u osvojenim gemovima: ").split())

if x==7 and (y==6 or y==5):
    print("Pobedio prvi teniser")
elif y==7 and (x==6 or x==5):
    print("Pobedio drugi teniser")
elif x==y and x<7 or x<=5 and y<=5 :
    print("Nije zavrsen set")
elif x==6 and y<=4:
    print("Pobedio prvi teniser")
elif y==6 and x<=4:
    print("Pobedio drugi teniser")
else:
    print("Neispravno")
