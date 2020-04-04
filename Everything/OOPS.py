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


'''Ratan            # need to verify
class:  logical entity
        Blue Print of object
        we can create multiple objects based on single blue print
        syntax: class {class name}
        
object: physical entity represent memory
                                            MM IMP:
                                            Function inside Class called Method
                                            constructor --> __init__  --> execute by itself
                                            method --> we have to call to execute this  
'''

#example 1
'''
#python 2.7  : class is not child class of object
class Myclass1:
    pass
class Myclass2():
    pass
class   Myclass3(object):
    pass

print(issubclass(Myclass1,object))      #false
print(issubclass(Myclass2,object))      #false
print(issubclass(Myclass3,object))      #true
'''

#python 3.7 : by default class is child class of object 
class Myclass1:
    pass
class Myclass2():
    pass
class Myclass3(object):
    pass
print(issubclass(Myclass1,object))          #true
print(issubclass(Myclass2,object))          #true
print(issubclass(Myclass3,object))          #true

#Example 2             
print('declaring function inside the class')
class Myclass:
    def disp1(self):    
        print('good morning')

    def disp2(self,name):       #see - to declare disp2 function belongs to class use "self"
        print('good evening: ',name)

c=Myclass()
c.disp1()
c.disp2('Ratan')

#???  IMP see-instance method vs. Static method vs. Class method

print('example 3')         #instance and static method
class Myclass:
    def m1(self):
        print('instance method')
    xgerf=20
    
    @staticmethod                   # must nedd this decorator to declare staticmethod
    def m2():
        print('static method')

c=Myclass()
c.m1()                      #to call instance method

Myclass.m2()                #to call static method

#example 4 - skip

print('example 5 : local variables, class variables, global variables')
i,j=100,200                         #to declare global variable
class Myclass():
    a,b=10,20                       #to declare class variables
    def add(self,x,y):              #to declare local variables

        print(i+j)                  # to access global variable
        print(x+y)                  # to access local variable
        print(self.a+self.b)        # to access class variable
c=Myclass()
c.add(50,60)

print('example 6 : same name of local , global and class variable')
i,j=100,200                                     #to declare global variable
class Myclass():
    i,j=10,20                                   #to declare class variables
    def add(self,i,j):                          #to declare local variables

        print(globals()['i']+globals()['j'])    # to access global variable
        print(i+j)                              # to access local variable
        print(self.i+self.j)                    # to access class variable
c=Myclass()
c.add(50,60)

#example 7 - skip

print('example 8 - named and nameless object')
class Myclass():
    def disp(self):
        print('how are you?')

c1=Myclass()                    #named object
c1.disp()

Myclass().disp()                #name less object

print('example 9') 
'''
id() : print memory location
is, is not : memory comparison : return boolean         #it compares data as well as memory location
== , !=  : data comparison : return boolean
in, not in : check data available or not : return boolean
'''

class Myclass():
    pass

c1=Myclass()
c2=Myclass()
c3=c1

print(id(c1))
print(id(c2))
print(id(c3))

print(c1 is c2)
print(c1 is c3)

print('example 10')      #class variable value is related to each object  
class Myclass():
    name='ratan'

c1=Myclass()
c2=Myclass()

print(c1.name)          #ratan

c1.name='durga'
print(c1.name)          #durga      

print(c2.name)          #ratan   
#c1.name is different than c2.name so when we chnage c1.name its doesnt affect c2.name

# see - what is the importance of self ?? 
 
print('example 11')           
#constructor -->  __init__  --> execute by itself when we create instance
class myclass:
    def m1(self):
        print('good morning')
    def __init__(self):
        print('0 arg constructor')

c1=myclass()                # when we create instance this will execute __init__ by it self
c1.m1()     

#IMP example 12                 # to convert local var into class var
class Myclass():
    def values(self,value1,value2):  #local variables(value1,value2) limited to this function only 
        print(value1)
        print(value2)

  #class variable    local variable
        self.value1=value1 
        self.value2=value2
    def add(self):
        print(self.value1+self.value2)

c1=Myclass()
c1.values(8,9)
c1.add()

#example 13
class Myclass():
    def m1(self):          
        print('class m1')
        self.m2(10)              #to call one method inside another method

    def m2(self,a):
        print('clas m2 value is ',a)

c1=Myclass()
c1.m1()

#example 14                             #constructor with local variable
class Myclass:
    name='durga'
    def __init__(self,name):
         print('good morning',name)
        print('good evening',self.name)

c=Myclass('ratan')              #give variable while creating instance bcoz __init__ has 1 variable

#example 15                     
#conversion of local var to class var
class operation:
    def __init__ (self,val1,val2):   #local variables(val1,val2) limited to this function only 
        print(val1)
        print(val2)

        self.val3=val1           #conversion of local var to class var
        self.val4=val2

    def add(self):
        print(self.val3+self.val4)

c=operation(10,20)
c.add()

#example 16      
class Emp:
    def __init__(self,eid,ename,esal):
         self.eid=eid
        self.ename=ename
        self.esal=esal

    def disp(self):
        print(self.eid,self.ename,self.esal)

c=Emp('ss','gg','aa')
c.disp()

#example 17         #__str__  -->  this will be executed when we print instance( here c instance)
                    # works only with return and string
#case 1
class Myclass:
    pass
c=Myclass
print(c)                     # this will print object memory location

#case 2
class Myclass:
    def __str__(self):       # this method will be called when we print object
        return 'ratan'
c=Myclass()
print(c)

#case 3                         # __str__ returns only string value
class Myclass:
    def __str__(self):
        return 10

c=Myclass()
#print(c)                       #__str__ returned non-string (type int)

#case 4
class Myclass:
    def __str__(self):
        print('ratan')          #__str__ works with return only so here with print it will give none

c=Myclass()
#print(c)                        __str__ returned non-string (type NoneType)

#example 18             #to exeute method with __str__
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal

    def __str__(self):
        return "emp id ={}, ename= {}, esal={}" .format(self.eid,self.ename,self.esal) #must be return and string

c=Emp('ss','gg','aa')
print(c)

#example 19                 __del__  --> executed when we del object
class Myclass():
    def __del__(self):
        print(" object destroyed")

#xx1=Myclass()
#xx2=Myclass()

#del xx1                         # this will execute __del__

#example 20             #to execute __del__ --> all same objects must be call to delete
class Mycalss():
    def __del__(self):
        print('object destroyed')

#c1=Myclass()
#c2=c1
#c3=c1

#del c1
#del c2                      # to execute __del__ all c1,c2,c3 must be del
#del c3                      # otherwise it will not execute __del__


print('Inheritance')               # getting properties from parent class
#exampe 1            #skip

#example 2       
#better to create child class objects so that we can access child and parents both methods
class Parent():
    def m1(self):
        print('parent m1() method')

class child(Parent):
    def m2(self):
        print('child m2 method')

p=Parent()
p.m1()

c=child()
c.m1()
c.m2()

#example 3
print('*to access parent class variable from child class when variabes name unique')
class Parent():
    a,b=10,20

class child(Parent):
    x,y=100,200
    def add(self,i,j):
        print(i+j)
        print(self.x+self.y)
        print(self.a+self.b)      
        #with self we can access parent class variables when variable names are different
c=child()
c.add(1000,2000)

#example 4
print('*IMP: to access parent class variable from child class when variabes name same')
a,b=500,5000
class Parent():
    a,b=10,20

class child(Parent):
    a,b=100,200
    def add(self,a,b):
        print(a+b)                              #to access local variable
        print(self.a+self.b)                    #to access class variable
        print(super().a+super().b)              #to access parent class variable
        print(globals()['a']+globals()['b'])    #to access global variable
c=child()
c.add(1000,2000)

#example 5 
print('*to access/call parent class method from child class method ')
class Parent():
    def m1(self):
        print('parent m1() method')

class child(Parent):
    def m2(self):
        super().m1()                #super() will call parent class method
        print('child m2 method')

c=child()
c.m2()

#example 6
print('*parent class constructor') 

#case 1                 
print('- only parent class has constructor')   
class Parent:
    def __init__(self):
        print("parent class constructor")
class Child(Parent):
    pass
c=Child()         #if child class doenst have constructor it will execute parent class constructor

#case 2                 
print('- parent class and child class both have constructor')   
class Parent:
    def __init__(self):
        print("parent class constructor")
class Child(Parent):
    def __init__(self):
        print("child class constructor")
c=Child()     #if child class has constructor it will execute child class constructor only by default


#case 3
print('#parent class and child class both have constructor-execute constructor of parent class')   
class Parent:
    def __init__(self,name):
        print("parent class constructor",name)
class Child(Parent):
    def __init__(self):
        super().__init__('durga')      #super() can execute parent constructor
        print("child class constructor")
        super().__init__('ratan')      #super() can execute parent constructor
c=Child()                     

#case 4
print('#parent class and child class both have constructor-execute constructor of any class')   
class Parent:
    def __init__(self,name):
        print("parent class constructor",name)
class grandchild(Parent):
    def grand_child():
        print('grandchild')
class Child(Parent):
    def __init__(self):
        Parent.__init__(self,'anu')      
    #method2:we can execute other class constructor this way as well
        grandchild.grand_child()         
    #method2:we can execute other class constructor this way as well
        print("child class constructor")
c=Child()   

#example 7           #within class - to access one method inside another method 
class Myclass():
    def disp1(self):
        print('private method')

    def disp2(self):
        print('this is disp2')
        self.disp1()

a=Myclass()
a.disp2()                   

print('inheritance types')
#1.single Inheritance           #mother has 1 child
class Parent:
    pass
class child(Parent):
    pass

#2.Multilevel Inheritance       # grandfather, father, child
class A:
    pass
class B(A):
    pass
class C(B):
    pass

#3.Multiple Inheritance     #father and mother has 1 child
class A:
    pass
class B:
    pass
class C(A,B):
    pass

#4.Hierachial Inheritance   #father has 2 child
class A:
    pass
class B(A):
    pass
class C(A):
    pass

#5.Hybrid inheritance    #combination of multiple and Hirerchial 

#example 7          Multilevel inheritance example

class A:
    def m1(self):
        print('m1 method')

class B (A):
    def m2(self):
        print('m2 method')

class C (B):
    def m3(self):
        print('m3 method')

c=C()
c.m1()
c.m2()
c.m3()

#example 8          hirarchial inheritance example
class Vehicle():
    def disp1(self):
        print('vehicle info')

class Car(Vehicle):
    def disp2(self):
        print('car info')

class Plane(Vehicle):
    def disp3(self):
        print('Plane info')
c=Car()
c.disp1()
c.disp2()

p=Plane()
p.disp1()
p.disp3()

#example 9              #multiple inheritance

class Parent1:
    def m1(self):
        print('parent m1 method')

class Parent2:
    def m2(self):
        print('parent m2 method')

class Child(Parent1,Parent2):
    def m3(self):
        print('child m3 method')

c=Child()
c.m1()
c.m2()
c.m3()

#example 10         #

class Person():
    def __init__(self,first,last):      #first,last = local var
        self.first=first                #making local variable to class variable so that other methods in this class can use it
        self.last=last

class Emp(Person):
    def __init__(self,first,last,id):
        super().__init__(first,last)        #to call parent class __init__
        Person.__init__(self,first,last)    #to call parent class __init__
        self.id=id                          #making local variable to class variable so that other methods in this class can use it

    def disp(self):
        print('Emp id={} Emp firstname={} Emp lastname={}' .format(self.id,self.first,self.last))

e1=Emp('ratan','durga',121212)
e1.disp()

#example 11         #to call by objects here e1         #already covered in past
class Person():
    def __init__(self,first,last):      #first,last = local var
        self.first=first                #making local variable to class variable so that other methods in this class can use it
        self.last=last

class Emp(Person):
    def __init__(self,first,last,id):
        super().__init__(first,last)        #to call parent class __init__
        Person.__init__(self,first,last)    #to call parent class __init__
        self.id=id                          #making local variable to class variable so that other methods in this class can use it

    def __str__(self):
        return 'Emp id={} Emp firstname={} Emp lastname={}' .format(self.id,self.first,self.last)

e1=Emp('ratan','durga',121212)
print(e1)

#example 12         #to check relation    
#to check instance 
class parent:
    pass

class child(parent):
    pass

p=parent()
c=child()

print(isinstance(p,parent))         #p has relation with parent class?        #yes.p is itself parent
print(isinstance(c,child))          #c has relation with child class?         #yes, c is itslef child
print(isinstance(c,parent))         #c has relation with parent class?        #yes, c is child of parent class
print(isinstance(c,object))         #c has relation with object ?             #yes, all parent class is child of object 
                                                                              #and c has relation with parent class
print(isinstance(p,object))         #p has relation with object?              #yes, all parent class is child of object
print(isinstance(p,child))          #p has relation with child?                 #no. it can go upward only no downward

#polymorphism

#example 1          
print('#over riding variables')
#case 1
class Parent:
    name='ratan'

class Child(Parent):
    name='anu'
c=Child()                       #here priority goes to child class name variable.
print(c.name)

#case 2
class Parent:
    name='ratan'

class Child(Parent):
    pass
c=Child()                       #here priority goes to Parent class name variable.
print(c.name)


print('#over riding methods')
#case 1
class Parent:
    def girl(self):
        print('red girl')

class Child(Parent):
    def girl(self):
        print('yellow girl')
c=Child()                       #here priority goes to child class method.
c.girl()

#case 2
class Parent:
    def girl(self):
        print('red girl')

class Child(Parent):
    pass

c=Child()                       #here priority goes to parent class method.
c.girl()

#example 3
print('*MM IMP real time scenario')
print('* calling object from another function')

class Parrot:
    def fly():
        print('parrot can fly')
    def swim():
        print('parrot can not swim')

class Fish:
    def fly():
        print('Fish can not fly')
    def swim():
        print('Fish can swim')

#create object
p=Parrot()
f=Fish()

#common intereface
def fly_test(animal):
    animal.fly()

#passing the objects
fly_test(Parrot)

#example 4    #another example

class Unicorn:
    def speed(self):
        print('Unicorn speed')

class Splendor:
    def speed(self):
        print('splendor speed')

u=Unicorn()
s=Splendor()

#common intereace
def bike_speed(name):
    name.speed()

bike_speed(u)

# encapsulation              #process of binding properties and methods as single unit
#example 1
print('* private class variable can access within class only')

class A():
    __a=10
    def disp(self):
        print(self.__a)

obj=A()
#print(obj.__a)              #__a is private so can not access outside class         
                             #'A' object has no attribute '__a'

obj.disp()                   #__a can be accessed with the help of another mehtod   #getter method

#example 2
print('* private method can access within class only')
class Myclass():
    def __disp1(self):
        print('private method')

    def disp2(self):
        print(' this is disp2')
        self.__disp1()

a=Myclass()
#a.__disp1()         #we can not call __disp1 outside the class        #'Myclass' object has no attribute '__disp1'

a.disp2()            #we can call __disp1 by calling disp2 bcoz __disp1 already called within class  #getter method


#example 3              #getter and setter method
class Emp():
    __eid=111

    def setEid(self,eid):       #setter method - which can update private var with setter method
        self.__eid=eid

    def getEid(self):           #getter method - to access private var with getter method
        print(self.__eid)

e=Emp()

#print(e.__eid)             'Emp' object has no attribute '__eid'

e.getEid()                  #to access private var
e.setEid(222)               #to update private variable
e.getEid()                  #to access private var

#example 4              #to access one class variable into another class
class A:
    num1,num2=100,200

class B():
    def add(self):
        a=A()                           #for every method create objet again
        print(a.num1+a.num2)
    def mul(self):
        a=A()                           #for every method create objet again
        print(a.num1*a.num2)

b=B()
b.add()
b.mul()

#better solution for above example
#example 5         #create object at class level so then we dont need to create object at method level again and again
class A:
    num1,num2=100,200

class B():
    a=A()                           #create object at class level so then we dont need to create object at method level again and again
    def add(self):
        print(self.a.num1+self.a.num2)
    def mul(self):
        print(self.a.num1*self.a.num2)

b=B()
b.add()
b.mul()


#abstract
from abc import ABC,abstractmethod
class Person(ABC):
    @abstractmethod
    def eat(self):
        pass

class Ratan(Person):
    def eat(self):
        print('5 idly')

class Durga(Person):
    def eat(self):
        print('4 idly')

r=Ratan()
r.eat()

d=Durga()
d.eat()