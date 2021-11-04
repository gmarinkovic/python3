# Напиши програм који за тачку у равни задату својим координатама испитује да ли припада задатом кругу и
# задатом правоугаонику чије су странице паралелне са координатним осама.
#
# Улаз: Са стандардног улаза учитавају се следећи реални бројеви (бројеви у истом реду су раздвојени једним
# размаком):
# • x, y - координате тачке,
# • x0, y0 - координате заједничког центра круга и правоугаоника,
# • r - полупречник круга,
# • w, h - дужина и ширина страница правоугаоника.
#
# Излаз: На стандардни излаз исписати два линије текста. У првој линији треба да пише jeste u krugu ако
# тачка (x, y) припада кругу са центром (x0, y0) полупречника r односно nije u krugu ако тачка не припада
# кругу. У другој линији треба да пише jeste u pravougaoniku ако тачка (x, y) припада правоугаонику чији
# је центар (тежиште) у тачки (x0, y0), чије су странице паралелне координатним осама и чија је дужина w тј.
# h, односно nije u pravougaoniku ако тачка не припада унутрашњости тог правоугаоника. Граница круга
# (кружница) и правоугаоника сматрају се њиховим делом.
#
# Пример
# Улаз
# 1 1
# 0 0
# 1
# 2 2
# Излаз
# nije u krugu
# jeste u pravougaoniku
import math

(x,y)  = input("Unesite koordinate ispitne tacke: ").split()
(x0,y0)= input("Unesite koordinate temene tacke kruga: ").split()
r      = int(input("Unesite poluprecnik kruga: "))
(w,h)  = input("Unesite duzinu i sirinu pravougaonika: ").split()

# proracun rastojanja od centra kruga trazene tacke (x-x0)^2 + (y-y0)^2 > r^2

f=pow(abs(int(x)-int(x0)),2)+pow(abs(int(y)-int(y0)),2)

if f >= pow(r,2):
    print("Tacka nije u krugu")
else:
    print("Tacka je u krugu")

if abs(int(x)) < abs(int(w)) and int(x)*int(w)>0 and abs(int(y))<abs(int(h)) and int(y)*int(h)>0:
    print("Tacka je u kvadratu")
else:
    print("Tacka je van kvadrata")
