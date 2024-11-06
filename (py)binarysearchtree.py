class Array:
    def __init__(elf):
        elf.stuff=[]
    def append(elf,insertstuff):
        elf.stuff += [insertstuff]
    def __str__(elf):
        return str(elf.stuff)
Test=Array()
print(Test)
Test=[1,2]
print(Test.stuff)