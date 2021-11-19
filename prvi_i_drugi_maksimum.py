# Bez nizova/lista...
#
# Написати програм којим се одређују највећа два различита броја од пет датих целих бројева.
#
# Улаз: На станадардном улазу налазе се 5 целих бројева, сваки у посебној линији.
#
# Излаз: Прва линија стандарног излаза садржи највећи број од датих 5 бројева. Друга линија стандардног
# излаза садржи други по величини цео број од датих 5 бројева. Aко су сви унети бројеви једнаки друга линија
# треба да садржи само знак ‘-’.
#
# Пример 1
# Улаз
# 2
# 7
# -4
# 7
# 3
# Излаз
# 7
# 3
#
# Пример 2
# Улаз
# 12
# 12
# 12
# 12
# 12
# Излаз
# 12
# -
def maksi(x,max1,max2):
    if max1 < x:
        max2=max1
        max1=x
    elif max2 < x != max1:
        max2=x
    return max1, max2

a = int(input("Uneti prvi broj: "))
max1=a
max2=0

b = int(input("Uneti drugi broj: "))
if max1 < b:
    max1=b
    max2=a

c = int(input("Uneti treci broj: "))
max1 , max2 = maksi(c,max1,max2)

d = int(input("Uneti cetvrti broj: "))
max1 , max2 = maksi(d,max1,max2)

e = int(input("Uneti peti broj: "))
max1 , max2 = maksi(e,max1,max2)

if a==b==c==d==e:
    max1=a
    max2="-"

print(max1)
print(max2)
