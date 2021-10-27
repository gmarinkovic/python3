# RAD SA VREMENIMA i njihovim pozicionim zapisima - HONEROVA SEMA

# Два стара другара су договорила да се нађу у центру града. Познато је време (у облику сата, минута и секунде)
# када је свако од њих дошао на састанак (оба времена су у једном дану). Напиши програм који одређује колико
# дуго је онај који је први стигао чекао оног другог.
# Улаз: Са стандардног улаза се уноси шест целих бројева (сваки је задат у посебном реду). Сат (између 0 и
# 23), минут (између 0 и 59) и секунд (између 0 и 59) доласка првог човека и сат, минут и секунд доласка другог
# човека. Подаци представљају исправно задате временске тренутке у оквиру једног дана.
# Излаз: На стандардни излаз исписати број сати, минута и секунди колико је онај другар који је први дошао
# чекао другог. Бројеве исписати у једном реду, раздвојене двотачком.
# Пример
# Улаз
# 3
# 45
# 20
# 7
# 23
# 50
#
# Излаз
# 3:38:30

def u_sekunde(sati,minute,sekunde):
    ukupnosekundi=sati*60*60+minute*60+sekunde
    return ukupnosekundi

def u_sat_min_sek(sekunde):
    sekunde_konacne=sekunde%60
    minute= (sekunde//60)%60
    sati= sekunde//3600
    return (sati,minute, sekunde_konacne)

sat1 = int(input())
minut1 = int(input())
sekunde1 = int(input())
sat2 = int(input())
minut2 = int(input())
sekunde2 = int(input())

vreme1= u_sekunde(sat1, minut1, sekunde1)
vreme2= u_sekunde(sat2, minut2, sekunde2)

vreme= abs(vreme1-vreme2)

(h,m,s) = u_sat_min_sek (vreme)

print(h,":",m,":",s)
