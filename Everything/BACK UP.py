#--------------------------------------------------------------------------------------
#ratan classes

print('***variable')
evalue,esalary,expect=10,20,30
evalue=esalary=expect=10

print('*re assigning variable value')
a=10
print(a)

a=100
print(a)

print('*delete variable')

v=10
print(v)
del v

print('***INPUT')

'''
print('* take input as string and then do concatenate')
a=input('A=')				#IMP:  Input takes all value as string
b=input('B=')				#thats why this example will give string as result (eg:1020)
print(a+b)

eid= int(input('eid:'))			# convert input value as int
ename=input('ename:')
esal=float(input('esal:'))		# convert input value as float

print('Example-1')
num1= input('Enter first num:')		
num2= input('Enter second num:')
total=num1+num2
print('total:',total)

# below example will give int as result

print('* take input as int and then do concatenate')
print('example-2')
num1= int(input('Enter first num:'))
num2= int(input('Enter second num:'))
total=num1+num2
print('total:',total)
'''

print('***Range')						# logic same as index
'''
Rule: start from first value upto second value and if third value is 
	  positive move left to right and if third value is negative then
	  move right to left 
'''
for x in range(5):
	print(x)

for x in range(6,10):
	print(x)

for x in range(14,20,3):
	print(x)

for x in range(22,14,-3):
	print(x)

for x in range(-10,-1,4):
	print(x)

for x in range(-15,-27,-5):
	print(x)

print('***Python identifiers - nomenclature of class,function rules')
'''
Rule 1 :a-z , A-Z , _    -should not start with numberic , should not allow special characters
Class Myclass123 - valid
Class 123Myclass - Invalid
Class Myclass_123 - valid
Class Myclass*123 - invalid

Rule 2 : case sensitive

Rule 3 : No lenght limit

Rule 4 : Duplicates not allowed				# duplicates allowed only in variable

Rule 5 : kewords not allowed
self=100 									#not allowed

Rule 6 : Possible to take pre defined class names as identifiers but not recommended
'''

print('***how to know length ')
print('- for string')
s='    ratan IT   '
print(len(s))

print('- for list')
l1=[10,'ratan',10.5]
print(len(l1))

print('***how to remove space')
print(s.strip()) 		#to remove space at begining and at the end
print(len(s.strip()))

print('***how to remove characters')
s1='@@@ratan IT####'					#characters can be remove at begining or end.. not from middle
print(len(s1))
print(s1.lstrip('@'))		# to remove @ at begining
print(s1.rstrip('#'))		# to remove # at the end
print(s1.rstrip('#').lstrip('@'))
print(s1.lstrip('IT'))		# i can not remove IT here because its in middle of string

print('***to check memory location and data comparison')
'''
id() : print memory location
is, is not : memory comparison : return boolean    		#it compares data as well as memory location
== , !=  : data comparison : return boolean
in, not in : check data available or not : return boolean
'''

print('- For string')
name1='ratan'
name2='anu'
name3='ratan'

print(id(name1))
print(id(name2))
print(id(name3))

print('**')
print(name1 is name2)				
print(name1 is name3)				#same string value-->save at same memory location thats why here its true
print(name1 is not name2)
print(name1 is not name3)

print('**')
print(name1==name2)
print(name1==name3)
print(name1!= name2)
print(name1!= name3)

print('**')
print('ra' in name1)
print('durga' in name1)
print('ra' not in name1)
print('durga' not in name1)

print('- For List')
L1=[10,20,30]
L2=[40,50,60]
L3=L1
L4=[40,50,60]

print(id(L1))
print(id(L2))
print(id(L3))
print(id(L4))

print('**')
print(L1 is L2)
print(L1 is L3)
print(L1 is not L2)
print(L1 is not L3)

print('**')
print(L1==L2)
print(L1==L3)
print(L2==L4)
print(L1!=L2)
print(L1!=L3)
print(L2!=L4)

print('**')
print(10 in L1)
print(100 in L1)
print(10 not in L1)
print(100 not in L1)

print('- for Dics')
d1={111:'ratan',222:'anu'}
d2={333:'ratan',444:'anu'}
d3=d1
d4={111:'ratan',222:'anu'}

print(id(d1))
print(id(d2))
print(id(d3))
print(id(d4))

print(d1 is d2)
print(d1 is d3)
print(d1 is not d2)
print(d1 is not d3)

print(d1==d2)		#data caomparison: compares both key,value
print(d1==d4)
print(d1!=d2)
print(d1!=d4)

print(111 in d1)	#check only keys avaiable or not
print(11 in d1)
print(111 not in d1)
print(11 not in d1)

print('***packing')
print('*convert 2 list into dics')
l1=[1,2,3,4]							 
l2=['ratan','durga','anu','ratanIT']
x=zip(l1,l2)			
d=dict(x)
print(d)

print('*convert 2 tuple into dics')
l1=(1,2,3,4)							 
l2=('ratan','durga','anu','ratanIT')
x=zip(l1,l2)			
d=dict(x)
print(d)

print('*convert 2 set into dics')
l1={1,2,3,4}							 
l2={'ratan','durga','anu','ratanIT'}
x=zip(l1,l2)			
d=dict(x)
print(d)

print('***Unpacking') 
print('-for list')		#List --> variables #it will break list and assigns values to variables
L1=[10,10.4,'ratan']
a,b,c=L1
print(a,b,c)
print(type(a),type(b),type(c))

#IMP
L2=[10,20,30]
#a,b=L2		#this will give an error, need exact number of variables for unpacking 

print('-for dics')
d1={1:'aaa',2:'bbb'}
a,b=d1
print(a,b)				# dics will unpack only keys

d2={1:'aaa'}
c=d2
print(c)

print('*see - advanced')
L2=[[1,2,'ratan'],[3,'tata']]
a,b=L2
print(type(a))
print(b)
print(b[1])

print('***to arrange by ACS/Desc')
print('*** to arrnage by any logic')
''' IMP
just to arrange by asc or desc ---> sort 			#it chnages object itself
to arrange with any other logic ---> sorted 		#it crates new object with changes
'''
print('-For List')
print('*arrange number in asc order')
a=[1,4,5,3,2]
a.sort()		
print(a)

print('*arrange alphabet in asc order')
b=['a','e','b','d','c']
b.sort() 	
print(b)

print('*arrange number in desc order')
e=[1,4,5,3,2]
e.sort(reverse=True) 		
print(e)

print('*arrange alphabet in desc order')
f=['a','e','b','d','c']
f.sort(reverse=True)		
print(f)

print('***IMP: if we declare 2 lists same then if we sort any one it will sort both in this case use sorted')

print('***sorted')
print('* arrange in ascending by sorted')
f=['a','e','b','d','c']
f1=sorted(f)

print('* arrange in descending by sorted')
f=['a','e','b','d','c']
f1=sorted(f,reverse=True)
print(f1)

print('*arrange given list by length')
i=['bcde','cd','def','a']
j=sorted(i,key=len)
print(j)

print('*arraneg by function')
def func(x): 
    return x % 7
L = [15, 3, 11, 7] 
m = sorted(L, key = func)
print(m)

print('*do sorting of heterogenous data')
l3=[10,20.85,'ratan']
#l3.sort() 					#heterogenous sorting not supported

print('-for Dics')
print('*arrange Dictionary ascending by key,value and items')
d1={1:'ratan',2:'durga',3:'anu',4:'surya'}
print(sorted(d1.keys()))
print(sorted(d1.values()))
print(sorted(d1.items()))

print('***arrange list in reverse order without using sort')
l1=[10,20,30]
l1.reverse()
print(l1)

print('-for list of Dictionary')  # almost same as list
from operator import itemgetter
list1=[ {'name':'akhil','year':1987, 'age':32},
        {'name':'palak','year':1993, 'age':27},
		{'name':'shiv','year':1985, 'age':39}
	  ]

list2=sorted(list1,key=itemgetter('year'))
print(list2)


print('***List datatype properties')
'''
1. represent group of objects :homogenus(same data type of objects) & heterogrnous( different data types of object)
example: homogenous L1=[10,20,30]  heterogenous L2=[10,'ratan',10.05]
2. indexing : forward and backward
3. duplicate objects allowed
4. mutabale: modifications are allowed
5. insertation order : e1,e2,e3 --> e1 e2 e3
'''
print('***to access data in (Nested/sub list/Multi dimension) List,tuple,set')
'''
IMP
to access data In dataframe use loc, iloc
'''

#      0	   1
L1=[[10,20],['ratan','tata']]
#    0  1    0  1 
print(type(L1[0]))
print(L1[0])
print(L1[1])

print(type(L1[1][1]))
print(L1[0][1])
print(L1[1][1])

print('***create another copy of list')
l1=[10,20,30]
l2=l1.copy()
print(l2)

print('-For list')
print('*add one entire list into another list')
l1=[10,20,30]
l2=[40,50,60]
l1.extend(l2)
print(l1)

print('*to add object at the end')
l1=[10,20,30]
l1.append(40)
print(l1)

print('*to add object by specific location')
l1=['ratan','anu']
l1.insert(1,'aaa')		#this will add at index 1
print(l1)
l1.insert(6,'bbb')		#this will add at index6 but we dont have index5 so it will add at the end
print(l1)

print('*to delete by object location')
l1=['ratan','durga',10,10.5]
l1.pop()			# by default it will remove last one
print(l1)
l1.pop(1)			# this will remobe index 1 object
print(l1)
#l1.pop(10)			# pop index out of range

print('*to delete by object value')
l1=[10,20,30]
l1.remove(20)
print(l1)

print('*in list to delete more than one objects same time')
l1=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150]
del l1[2]
print(l1)
del l1[1:4]
print(l1)
del l1[1:4:2]
print(l1)
del l1[:2]
print(l1)
del l1[:]
print(l1)

print('*in list to delete all objects') 
l1=[10,20,30]
l1.clear()
print(l1)

print('-for Dict')
print('*in dict to add object at the end')
d3={}
d3[111]='ratan'
d3[222]='anu'
d3[333]='ratan'
print(d3)

print('*to remove last key/particular key from dics')
d1={1:'aaa',2:'bbb',3:'ccc'}
d1.popitem()	# this will remove last item fron dics
print(d1)
d1.pop(2)		#this will remove key 2 from dics
print(d1)

print('*to remove all objects from dics')
d1={1:'aaa',2:'bbb',3:'ccc'}
d1.clear()
print(d1)

print('*to add one dict into another dict')
#method 1
d1={1:'aaa',2:'bbb'}
d2={3:'ccc',4:'ddd'}
d1.update(d2)
print(d1)

#method 2
d1={1:'aaa',2:'bbb'}
d2={3:'ccc',4:'ddd'}
x={**d1,**d2}
print(x)

print('***get maximum and minimum values in list')
l1=[10,20,30]
print(max(l1))
print(min(l1))

l2=['ratan','anu','durga']		#decide by ASCI value
print(max(l2))		
print(min(l2))

l3=[10,'ratan']				#TypeError: '>' not supported between instances of 'str' and 'int'
#print(max(l3))				# can not compare heterogenous objects	
#print(min(l3))				# can not compare heterogenous objects

print('* get maximum and minimum values in dics')
d1={1:'ratan',2:'durga',3:'anu',4:'surya'}
print(max(d1))
print(min(d1))

d2={'ratan':1,'durga':2,'anu':3,'surya':4}
print(max(d2))
print(min(d2))

#doest work with heterogenous dics
d3={1:'ratan',2:'durga','anu':3,'surya':4}	#TypeError: '>' not supported between instances of 'str' and 'int'
#print(max(d3))
#print(min(d3))

print('* get maximum and minimum values between 2 numbers')
print(max(2,10))

print('***Dics properties') 
'''
key:value    key=obj  	value=obj   :both together called item
{key:value,key:value}
keys:unique		values:duplicated
mutable: it allows modification
'''
print('Dict keys must be immutable(tuple,number,string) data type')
print('Dict values can be any data type')

#d1={[1,2]:'ratan',222:'anu',333:'durga'}		#list not allowed as dict key
print(d1)
#TypeError: unhashable type: 'list'

d1={111:['ratan','tata'],222:'anu',333:'durga'}		#list allowed as dict values
print(d1)

print('***override')
print('-Dics')
d3={}
d3[111]='ratan'
d3[222]='anu'
d3[333]='ratan'
d3[111]="repeat"		# if we try to enter same key again it will override that key and value
print(d3)

print('***None')			# None allowed in keys and values both
d2={None:None}
print(d2)

print('***Number systems')
'''
binary : base 2
octal  : base 8
decimal : base 10
Hexa decimal : base 16

binary system: allows 0 and 1
octal form: allows 0 to 7
decimal : allows 0 to 9
hexa decimal: allows 0 to 9 and a to f
'''

print('* to get ASCI values')
print('see-ASCI value')
c=5
#print(ord(c))

c=f
#print(ord(c))

print('*to get binary value')
print('binary values')
c=112
print(bin(c))

print('*to get octal value')
print('octal values')
c=20
print(oct(c))

print('*to get hexa decimal value')
print('hexa deciaml values')
c=20
print(hex(c))

print('***convert Datatypes')
print("*to convert int/float to string")
#x=str(y)

print("*to convert List to Tuple")
List1=['a','b','c','d']
Tuple1=tuple(List1)
print(Tuple1)

print("*To convert Tuple to List")
Tuple1=('a','b','c','d')
List1=list(Tuple1)
print(List1)

print("*to convert List to set")
List1=['a','b','c','d']
set1=set(List1)
print(set1)

print("*to convert set to list")
set1={'a','b','c','d'}
List1=list(set1)
print(List1)

print("*to convert Tuple to set")
Tuple1=('a','b','c','d')
set1=set(Tuple1)
print(set1)

print("*to convert Tuple to Dics ")
Tuple1=('a','b','c','d')
Dict2={i:i*2 for i in Tuple1}
print(Dict2)

print('* to convert int to string')
a=234
b=str(a)
print(type(b))

print('*to convert int to list')



print('*to convert string to list')
a='abc'
b=list(a)
print(type(b))

print('*to convert list to string')
a=['a','b','c']
b=str(a)
print(type(b))
print(b)

# Treenode



# Listnode 
# length?


#SQL pivot


print('***matrix')
print('*to create multi dimension matrix')
# val = [0] * n  								#n is row
# for x in range (n):
#     val[x] = [0] * m  						#m is column
# print(val)

# print('*to access value in matrix')
# val[1][2] 				# row 1, column 2

# print('*to add 1 to all rows')
# for m1 in list(range(m)):
#     val[a][m1]=val[a][m1]+1

# for n1 in list(range(n)):
#     val[n1][b]=val[n1][b]+1

print('*to find no of rows and columns')
a=[[1,1,0,1],[1,0,1,0],[0,0,0,1]]
print(len(a))						# to find no of rows
print(len(a[0]))					# to find no of columns

print('***to find max/min in row and column')
matrix = [[7,8],[1,2]]
x=len(matrix)
y=len(matrix[0])
col=[]
col1=[]
for a in range(x):
    print(min(matrix[a]))			#get min value in row

for b in range(y):
    for a in range(x):
        col1.append(matrix[a][b])
    col.append(max(col1))
	#get max value in column
    col1=[]
print(col)

print('*calendar')
import calendar
c=calendar.TextCalendar(calendar.MONDAY)
str=c.formatmonth(2019,8)
#print(str)

print('*string to timestamp - strptime')
from datetime import datetime
str = '9/15/18'
x = datetime.strptime(str, '%m/%d/%y')
print(x)

str='02,aug,2010'
x=datetime.strptime(str,'%d,%b,%Y')
print(x)

#datetime(year,month,day)
import datetime
y=datetime.datetime(2020,6,18)
print(y)

print('*to convert timestamp in different format')
import datetime
y=datetime.datetime(2020,6,18).strftime('%A')
y=datetime.datetime(2020,6,18).strftime('%b/%d/%Y')
print(y)

print('*to convert from one date format to another')
from datetime import datetime
x=datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')
print(x)

print('*todays date')
from datetime import datetime
y=datetime.today().strftime('%c')
print(y)
