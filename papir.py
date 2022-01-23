# Написати програм који израчунава масу одређеног броја одштампаних књига,
# да би издавачка кућа знала коју носивост камиона треба да наручи.
#
# Улаз:
# • Природан број brojKnjiga        (1 ≤ brojKnjiga ≤ 1000),        број одштампаних примерака књиге.
# – Природан број brojStranica      (30 ≤ brojStranica ≤ 500),      број страна једне књиге;
# – Природан број duzinaStranice    (50 ≤ duzinaStranice ≤ 297),    дужина листа тј. стране задата у милиметрима;
# – Природан број sirinaStranice    (50 ≤ sirinaStranice ≤ 210),    ширина листа тј. стране задата у милиметрима;
# – Реалан број masaPapira          (50 ≤ masaPapira ≤ 100),        маса папира у грамима по квадратном метру.
# – Реалан број masaKorica          (10 ≤ masaKorica ≤ 100),        маса корица једне књиге у грамима;
#
# Излаз:
# • Реалан број који представља укупну масу књига у килограмима, заокружен на 3 децимале.
#
# Пример
# Улаз
# 850
# 193
# 260
# 200
# 80.0
# 25.0
# Излаз
# 364.242

brojKnjiga      = int(input("Unesi broj knjiga: "))
brojStranica    = int(input("Unesi broj stranica jedne knjige: "))
duzinaStranice  = int(input("Unesi duzinu stranice u mm: "))
sirinaStranice  = int(input("Unesi sirinu stranice u mm: "))
masaPapira      = float(input("Unesi masu papira u gramima po kvadratnom metru: "))
masaKorica      = float(input("Unesi masu korica u gramima po kvadratno metru: "))

brojListova= brojStranica/2 if brojStranica%2 == 0 else (brojStranica+1)/2

masaStr = brojListova * (duzinaStranice * sirinaStranice)/1000000 * masaPapira
masaKor = 2 *           (duzinaStranice * sirinaStranice)/1000000 * masaKorica
masaKnjige = brojKnjiga * (masaStr + masaKor) /1000
print("Masa lista knjige je: "+"{:.2f}".format(masaStr)+" grama")
print("Masa korica knjige je: "+"{:.2f}".format(masaKor)+" grama")
print("Masa svih knjiga je "+"{:.3f}".format(masaKnjige)+" kilograma")
