#https://github.com/gurupratap-matharu/Bike-Rental-System
 
print("***CLASS")
#https://www.youtube.com/watch?v=qSDiHI1kP98

print("***class structure")
class abc:
	def __init__(self,value2):
		self.value1=value2
mine=abc('value of value1')
print(mine.value1)

print("***variables")
#to create class
class School:
#class variable (properties name and values both are 
#same for instances)
	song="jan gana mana"
	fund="govt of india"

	print("***instance variables") #(when properties name same but 
	#values different for instances)
	def __init__(self,first_langugae,managed_by):
		self.first_langugae=first_langugae
		self.managed_by=managed_by

#see 
#(when properties name are different for any instance)
	def border_country(self,country):
		pass

#to create object
Gujarat=School('gujarati','govt of Gujarat')
Karnataka=School('kannada','govt of Karnataka')

#to access object properties
print(Gujarat.song)
print(Karnataka.first_langugae)
#see 
#print(Gujarat.border_country('india'))

print("***Encapsulation") #(to make variable/function private for class
#that means can not access value / can not call)
#define by double underscore(__)
#https://www.youtube.com/watch?v=TFLo9m0jFEg
class Encapsulation:
	def __init__(self):
		self.a=123
		self._a=456
		self.__a=789
Encaps=Encapsulation()

print(Encaps.a)
print(Encaps._a)
# can not access __a value
#print(Encaps.__a)

#see
#to access __a value 
print(Encaps._Encapsulation__a)

print("***example without encapsulation")
class Car1:
	def __init__(self,speed,color):
		self.speed=speed
		self.color=color
ford=Car1(200,'red')
honda=Car1(250,'blue')
audi=Car1(300,'balck')
# here i can access speed value  
print(ford.speed) 


print("***example with encapsulation")
class Car2:
	def __init__(self,speed,color):
		self.__speed=speed
		self.__color=color
ford=Car2(200,'red')
honda=Car2(250,'blue')
audi=Car2(300,'balck')
#can not access __speed value from class
#print(ford.__speed)

#getter and setter with encapsulation
class Car2:
	def __init__(self,speed,color):
		self.__speed=speed
		self.__color=color

	def set_speed(self,value):
		self.__speed = value

	def get_speed(self):
		return self.__speed

	def __get_speed2(self):
		return self.__speed

ford=Car2(200,'red')
honda=Car2(250,'blue')
audi=Car2(275,'balck')
  
ford.set_speed(300)
ford.__speed=400
# can not access __speed atribute but if i assign that value
#to function by using return i can access function value
print(ford.get_speed())

print("***IMP")
print("can not access function get_speed2 value because its private")
#print(ford.get_speed2())
print("can not call get_speed2 because its private")
#ford.get_speed2()

print("***single inheritance")
#parent class
class Father:
	def __init__(self,fname,lname):
		self.fname=fname
		self.lname=lname
	def printname(self):
		print(self.fname,self.lname)

x=Father('akhil','shah')
x.printname()

#to create child class
class Son(Father):
	pass
y=Son('palak','shah')
y.printname()

print("***Multiple Inheritance")
#example 1

#parentclass1
class Person:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  

     #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
   
#parentclass2
class Student: # Person is the  
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  

#childclass  
class Resident(Student,Person):
# you have to give all variables from all parent
# we can change name but number of variables and sequence will remain same  
    def __init__(self, name, age, id):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id)  
    
# Create an object of the subclass  
resident1 = Resident('John', 30, '102')  
resident1.showName()  
print(resident1.getId())  


#example 2
class A:  
    def __init__(self):  
        self.name = 'John'  
        self.age = 23  
  
    def getName(self):  
        return self.name  
  
class B:  
    def __init__(self):  
        self.name = 'Richard'  
        self.id = '32'  
  
    def getName(self):  
        return self.name  
  
class C(A, B):  
    def __init__(self):  
        A.__init__(self)  
        B.__init__(self)  
  
    def getName(self):  
        return self.name  
  
C1 = C()  
print(C1.getName())  

'''
In the constructor of C, the first constructor called 
is the one of A. So, the value of name in C becomes 
same as the value of name in A. But after that, when 
the constructor of B is called, the value of name in 
C is overwritten by the value of name in B. So, the 
name attribute of C retains the value ‘Richard’ when 
printed. 
'''

print("***Multilevel Inheritance")
class Base(object):       
    # Constructor 
    def __init__(self, name): 
        self.name = name 
  
    # To get name 
    def getName(self): 
        return self.name 
  
#Inherited or Sub class (Note Person in bracket) 
class Child(Base):       
    # Constructor 
    def __init__(self, name, age): 
        Base.__init__(self, name) 
        self.age = age 
  
    # To get name 
    def getAge(self): 
        return self.age 
  
# Inherited or Sub class (Note Person in bracket) 
class GrandChild(Child):       
    # Constructor 
    def __init__(self, name, age, address): 
        Child.__init__(self, name, age) 
        self.address = address 
  
    # To get address 
    def getAddress(self): 
        return self.address         
  
# Driver code 
g = GrandChild("Geek1", 23, "Noida")   
print(g.getName(), g.getAge(), g.getAddress())

