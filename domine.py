# Зоран има две домине. На свакој домини су тачкицама представљене две цифре од 1 до 9.
# Напиши програм који одређује највећи број који Зоран може написати помоћу своје две домине
# (сваку од њих може окренути како жели и домине може поређати како жели).
#
# Улаз: Први ред стандардног улаза садржи бројеве на првој домини (раздвојене размаком),
# а други ред садржи бројеве на другој домини.
#
# Излаз: На стандардни излаз исписати тражени највећи број.
#
# Пример 1
# Улаз
# 2 3
# 1 6
# Излаз
# 6132
#
# Пример 2
# Улаз
# 1 9
# 3 4
# Излаз
# 9143
#
# Пример 3
# Улаз
# 6 2
# 3 6
# Излаз
# 6362

# ucitavamo cifre na dve domine
d1_str = input("Unesi parove sa prve domine: ").split()
d11, d12 = int(d1_str[0]), int(d1_str[1])
d2_str = input("Unesi parove sa druge domine: ").split()
d21, d22 = int(d2_str[0]), int(d2_str[1])
# odredjujemo vecu i manju cifru na prvoj domini
m11 = max(d11, d12)
m12 = min(d11, d12)
# odredjujemo vecu i manju cifru na drugoj domini
m21 = max(d21, d22)
m22 = min(d21, d22)
# odredjujemo bolji redosled domina leksikografskim poredjenjem parova
# (m11, m12) i (m21, m22)
if m11 > m21 or (m11 == m21 and m12 > m22):
    print(m11, m12, m21, m22)
else:
    print(m21, m22, m11, m12)
