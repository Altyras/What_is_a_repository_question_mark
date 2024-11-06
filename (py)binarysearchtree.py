from numpy import median


Stuff=[]
Stuff=[1,2,3,4,5,6,7,8,9,10]
median(Stuff)
print(median(Stuff))
print(median(Stuff)%5)
if (median(Stuff) % 5 == 0.5):
    print("Hiphip")
else:
    print("Horray!")