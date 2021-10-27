# RAD SA UGLOVIMA i njihovim pozicionim zapisima
#
# Марија је нашла географске координате на којима се налази закопано благо, међутим њен GPS уређај подржава географске координате унете као децимални број степени, док су координате које она има дате у броју
# степени, минута и секунди. Напиши програм који ће Марији помоћи да преведе координате.
# Улаз: Са стандардног улаза уносе се три цела броја:
# • st (0 ≤ st < 360) - број степени
# • min (0 ≤ min < 60) - број минута
# • sek (0 ≤ sek < 60) - број секунди
# Излаз: На стандардни излаз исписати један реалан број који представља угао у степенима (толеранција грешке је 10−5).
#
# Пример
# Улаз
# 18
# 19
# 20
#
# Излаз
# 18.32222

stepeni=int(input("Unesi broj stepeni kao celobrojnu vrednost: "))
minute=int(input("Unesi broj minuta kao celobrojnu vrednost: "))
sekunde=int(input("Unesi broj sekundi kao celobrojnu vrednost: "))

stepeni_decimalni=stepeni + minute/60 + sekunde/3600

print(format(stepeni_decimalni,".5f"))
