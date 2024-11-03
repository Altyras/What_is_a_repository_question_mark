class MyStuff:
    x=360

p1 = MyStuff()
print(p1)
print(p1.x)
a=None
class Pawn:
    def __init__(pawn,name,age,race):
        global a
        pawn.name = name
        a=pawn.name
        pawn.ae = age
        pawn.x=0
        pawn.y=0
        pawn.race=race
    def __str__(deb):
        return f"{deb.name},\tAge:{deb.ae},\tPositionX:{deb.x},\tPositionY:{deb.y}"
    def hello(deb,P,I):
        print(P+ deb.name, I)
    def x_incrementby1(pawn,I):
        pawn.x+=I
    def arebothpawnshere(pawn,deb,i=0):
        if pawn.x == deb.x and pawn.y == deb.y:
            print(f"I am here with {deb.name}")
        else:
            print(f"Nah I'm not with {deb.name}")
        if i == 1:
            print(f"{pawn}\n{deb}")
    def areboththesamename(pawn,deb,i=0):
        if pawn.name != deb.name:
            if i == 1:
                print("I",pawn.name,"do not share the same name with "+a, end=" ")
            return False
        else:
            if i == 1:
                print("I",pawn.name,"share the same name with "+a, end=" ")
            return True
    def moveto(pawn,deb,i=0):
        if (pawn.x and pawn.y) < (deb.x and deb.y):
            pawn.x +=1;pawn.y += 1
            if i==1:
                print(1,pawn.x,pawn.y)
        elif (pawn.x and pawn.y) > (deb.x and deb.y):
            pawn.x -=1; pawn.y -= 1
            if i==1:
                print(2,pawn.x,pawn.y)
        elif (pawn.x < deb.x) and (pawn.y > deb.y):
            pawn.x += 1; pawn.y -=1
            if i==1:
                print(3,pawn.x,pawn.y)
        elif (pawn.x > deb.x) and (pawn.y < deb.y):
            pawn.x -= 1; pawn.y +=1
            if i==1:
                print(4,pawn.x,pawn.y)
        elif pawn.x < deb.x:
            pawn.x +=1
            if i==1:
                print(5,pawn.x,pawn.y)
        elif pawn.x > deb.x:
            pawn.x -=1
            if i==1:
                print(6,pawn.x,pawn.y)
        elif pawn.y < deb.y:
            pawn.y +=1
            if i==1:
                print(7,pawn.x,pawn.y)
        elif pawn.y > deb.y:
            pawn.y -=1
            if i==1:
                print(8,pawn.x,pawn.y)
            



Cael = Pawn("Loverdale", 17, "Ashoid")
Poro=Pawn("Politos", 20, "Ashoid")

print(Cael.name)
print(Cael.ae)

Cael.x+=1
Cael.y=2
Cael.x_incrementby1(27)
print(Cael)

Cael.hello("Hi I'm ","an " + Cael.race)

Cael.arebothpawnshere(Poro)
Cael.areboththesamename(Poro)

if Cael.areboththesamename(Poro):
    print(f"And yes that is {Cael.areboththesamename(Poro,1)}")
else:
    print(f"or to simply: {Cael.areboththesamename(Poro,1)}")

for i in range(210):
    Cael.moveto(Poro)
    Poro.moveto(Cael,1)

Cael.arebothpawnshere(Poro,1)

print(i)
