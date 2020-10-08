class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def change_name(self,new_name):
        self.name=new_name

    def older(self):
        self.age=self.age+1

    def younger(self):
        self.age=self.age-1

p1 = Person('john',23)
print(p1.name)
p1.change_name('bob')
print(p1.name)
p1.older()
print(p1.age)
p1.older()
print(p1.age)
p1.younger()
print(p1.age)






