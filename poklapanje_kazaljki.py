# Ако сат показује тачно x сати, написати програм који одређује после колико минута ће се први пут поклопити
# велика и мала казаљка.
#
# Улаз: Број сати од 0 до 11.
# Излаз: У минутима заокруженим на најближу целобројну вредност од 0 до 60.
#
# Пример 1
# Улаз
# 2
# Излаз
# 11
#
# Пример 2
# Улаз
# 11
# Излаз
# 60

# ucitavamo vreme

h= int( input( "Unesi koliko je sati ( od 0 do 11) : "))

for i in range (1,61):

    # ugao miutne kazaljke se svakog minuta pomeri za 6 stepeni tj za 60 minuta se obrne za 360 stepeni
    min= i*6

    # satna kazaljka se u jednom satu tj njegovih 30 stepeni za svaki njen minut pomeri 60-ti deo od 30 stepeni
    # ugao u satne kazaljke ( svaki sat kazaljka se pomeri za 360/12=30 stepeni )
    ugaoSatneKazaljke = h*30
    sat = float(ugaoSatneKazaljke) + 30/60*i
    
    if (sat%6 == 0) and (min == (sat//6)*6):
        print("Do poklapanja kazaljki doslo je u " + str(i) + " minuti")
        break
    if ((sat%6) != 0) and (min == (((sat//6)+1)*6)):
        print("Do poklapanja kazaljki doslo je u "+str(i)+ " minuti")
        break
