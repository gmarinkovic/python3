# Дат је квадар чије су ивице паралелне координатним осама.
# Одредити запремину дела тог квадра који припада
# првом октанту (део простора у коме су све координате позитивне).
#
# Улаз: Са стандардног улаза учитава се 6 целих бројева који представљају редом 3 координате једног темена,
# затим 3 координате другог темена исте просторне дијагонале квадра.
#
# Излаз: На стандардни излаз исписује се један цео број - запремина дела квадра у првом октанту.
#
# Пример 1
# Улаз
# -2
# 4
# 1
# 3
# 2
# 7
# Излаз
# 36
#
# Пример 2
# Улаз
# 9
# 2
# -5
# 1
# 6
# -2
# Излаз
# 0
import math

x1 , y1, z1 = map(int,input("Unesite prvu temenu tacku sa celobrojnim koordinatama kvadra u prvom oktantu: ").split())
x2 , y2, z2 = map(int,input("Unesite drugu temenu tacku sa celobrojnim koordinatama kvadra u prvom oktantu: ").split())

if x1 <=0 :
    x1=0
elif x2<=0:
    x2=0
elif y1<=0:
    y1=0
elif y2<=0:
    y2=0
elif z1<=0:
    z1=0
elif z2<0:
    z2=0

v= math.ceil(abs(x1-x2) * abs(y1-y2) * abs(z1-z2))
print("Zapremina je : "+ str(v))
