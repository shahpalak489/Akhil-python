#Example 2             #declaring function inside the class
class Myclass:
    def disp1(self):    
        print('good morning',self)

    def disp2(hi,name):       #see - to declare disp2 function belongs to class use "self"
        print('good evening: ',hi)

c=Myclass()
c.disp1()
c.disp2('Ratan')