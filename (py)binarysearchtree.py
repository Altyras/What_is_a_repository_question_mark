class Array:
    def __init__(elf):
        elf.stuff=[]
    def append(elf,insertstuff):
        elf.stuff += [insertstuff]
    def __str__(elf):
        return str(elf.stuff)
Test=Array()
print(Test)
Test.append(1)
Test.append(2)
print(Test.stuff)

#just remaking the append function, don't mind