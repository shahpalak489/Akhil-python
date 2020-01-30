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
class   Myclass3(object):
    pass
print(issubclass(Myclass1,object))          #true
print(issubclass(Myclass2,object))          #true
print(issubclass(Myclass3,object))          #true

#Example 2             #declaring function inside the class
class Myclass:
    def disp1(self):    
        print('good morning')

    def disp2(self,name):       #see - to declare disp2 function belongs to class use "self"
        print('good evening: ',name)

c=Myclass()
c.disp1()
c.disp2('Ratan')

#???  see-instance method vs. Static method vs. Class method

#example 3         #instance and static method
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

#example 5 : local variables, class variables, global variables
i,j=100,200                         #to declare global variable
class Myclass():
    a,b=10,20                       #to declare class variables
    def add(self,x,y):              #to declare local variables

        print(i+j)                  # to access global variable
        print(x+y)                  # to access local variable
        print(self.a+self.b)        # to access class variable
c=Myclass()
c.add(50,60)

#example 6 : same name of local , global and class variable
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

#example 8 - named and nameless object
class Myclass():
    def disp(self):
        print('how are you?')

c1=Myclass()                    #named object
c1.disp()

Myclass().disp()                #name less object

#example 9 
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

#example 10             # class variable value is related to each object  
class Myclass():
    name='ratan'

c1=Myclass()
c2=Myclass()

print(c1.name)          #ratan

c1.name='durga'
print(c1.name)          #durga      

print(c2.name)          #ratan   #c1.name is different than c2.name so when we chnage c1.name its doesnt affect c2.name

# see - what is the importance of self ?? 
 
#example 11           #constructor -->  __init__  --> execute by itself when we create instance
class myclass:
    def m1(self):
        print('good morning')
    def __init__(self):
        print('0 arg constructor')

c1=myclass()                # when we create instance this will execute __init__ by it self
c1.m1()     

#IMP example 12                 # to convert local var into class var
class Myclass():
    def values(self,value1,value2):         #local variables(value1,value2) limited to this function only 
        print(value1)
        print(value2)

        self.value1=value1          # convert local variable into class variable so that other functions can also use them
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
        self.m2(10)                         #to call one method inside another method

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

c=Myclass('ratan')                          #give variable while creating instance bcoz __init__ has 1 variable

#example 15                     #conversion of local var to class var
class operation:
    def __init__ (self,val1,val2):          #local variables(val1,val2) limited to this function only 
        print(val1)
        print(val2)

        self.val1=val1                      #conversion of local var to class var
        self.val2=val2

    def add(self):
        print(self.val1+self.val2)

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

#example 17                    #__str__  -->  this will be executed when we print instance, works only with return and string

#case 1
class Myclass:
    pass
c=Myclass
print(c)                        # this will print object memory location

#case 2
class Myclass:
    def __str__(self):          # this method will be called when we print object
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
        return "emp id ={}, ename= {}, esal={}" .format(self.eid,self.ename,self.esal)          #must be return and string

c=Emp('ss','gg','aa')
print(c)

#example 19                 __del__  --> executed when we del object
class Myclass():
    def __del__(self):
        print(" object destroyed")

xx1=Myclass()
xx2=Myclass()

del xx1                         # this will execute __del__

#example 20             #to execute __del__all same objects should be del

class Mycalss():
    def __del__(self):
        print('object destroyed')

c1=Myclass()
c2=c1
c3=c1

del c1
del C2                      # to execute __del__ all c1,c2,c3 must be del
del c3                      # otherwise it will not execute __del__





