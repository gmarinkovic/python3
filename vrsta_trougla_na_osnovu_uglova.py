# Датa су три конвексна угла изражена у степенима и минутима. Написати програм којим се проверава да ли
# то могу бити углови троугла, и ако могу какав је то троугао у односу на углове (оштроугли, правоугли или
# тупоугли).
#
# Улаз: Са стандардног улаза уноси се шест целих бројева, сваки у посебној линији. Бројеви представљају
# три угла изражена у степенима. Подаци представљају исправно задате углове, степени и минути одређују
# исправно записане углове у интервалу од 0 степени и 0 минута, до 180 степени и 0 минута (минути су увек
# број између 0 и 59).
#
# Излаз: Једна линија стандарног излаза која садржи реч ostrougli, pravougli или tupougli, ако троугао са
# датим угловима постоји, у зависности од врсте троугла, или реч ne ако не постоји троугао са датим угловима.
#
# Пример
# Улаз
# 35 23
# 92 37
# 52 0
# Излаз
# tupougli

a1 , a2 =map(int,input("Uesi prvi ugao trougla (stepeni minuti): ").split())
b1 , b2 =map(int,input("Uesi prvi ugao trougla (stepeni minuti): ").split())
c1 , c2 =map(int,input("Uesi prvi ugao trougla (stepeni minuti): ").split())

if (a1+b1+c1)*60+(a2+b2+c2)==180*60:
    if ((a1>=90 and a2>0) or (b1>=90 and b2>0) or (c1>=90 and c2>0)):
        print("Tupougli")
    elif (a1==90 and a2==0) or (b1==90 and b2==0) or (c1==90 and c2==0):
        print("Pravougli")
    else:
        print("Ostrougli")
else:
    print("Posto zbir uglova trougla mora biti 180 stepeni, niste uneli odgovarajuce uglove!")
