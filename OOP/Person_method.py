class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self):
        print("Nama : " + self.name)
        print("Age :" , self.age)
        print("Address : " + self.address)

orang = Person("Nussa",10,"Jln. Kamboja")
orang1 = Person("Jordan",18,"Jln. Slipi")
orang.info()
orang1.info()
