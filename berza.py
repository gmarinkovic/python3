# Трговац на берзи је током једне радне недеље сваки дан или остваривао зараду или је губио новац. Од свих
# дана у којима је нешто зарадио, одредити дан у коме је најмање зарадио и вредност коју је тог дана зарадио
# (ако је више таквих дана, пријавити први) или пријавити да је свих дана губио новац.
#
# Улаз: Са стандардног улаза уноси се 5 целих бројева из интервала [−10000, 10000] (износи које је трговац
# остварио у понедељак, уторак, среду, четвртак и петак), сваки у посебном реду.
#
# Излаз: Ако је трговац у неком дану остварио зараду (износ је строго већи од нуле), на стандардни излаз
# у првом реду исписати најмањи износ зараде који је остварен током недеље и у другом реду ознаку дана
# (PON, UTO, SRE, CET или PET) у коме је остварен тај најмањи профит. Ако ниједан дан није остварена зарада,
# исписати ред који садржи само карактер -.
#
# Пример 1
# Улаз
# 3200
# -420
# -10
# 1350
# 5670
# Излаз
# 1350
# CET
#
# Пример 2
# Улаз
# -4700
# -360
# -1000
# -1550
# -3245
# Излаз
# -

a= int(input("Uneti zaradu za prvi dan: "))
b= int(input("Uneti zaradu za drugi dan: "))
c= int(input("Uneti zaradu za treci dan: "))
d= int(input("Uneti zaradu za cetvrti dan: "))
e= int(input("Uneti zaradu za peti dan: "))
potvrda=0
min1=10000
dan=""

if a>0:
    potvrda=1
    if a<min1:
        min1=a
        dan = "PON"

if b>0:
    potvrda=1
    if b < min1:
        min1 = b
        dan = "UTO"

if c>0:
    potvrda=1
    if c < min1:
        min1 = c
        dan = "SRE"

if d>0:
    potvrda=1
    if d < min1:
        min1 = d
        dan = "CET"

if e>0:
    potvrda=1
    if e < min1:
        min1 = e
        dan = "PET"

if potvrda :
    print(min1)
    print(dan)
else:
    print("-")
