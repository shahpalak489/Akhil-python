print("**Comprehensions**")
print("**List Comprehensions**")

l1=[x for x in range(5)]
print(l1)

l2=[x+5 for x in range(5,15,3)]
print(l2)

tuple1=(1,2,3,4,5)
x=[i for i in tuple1]
# same as for i in List1:
#             if....
#			print(i)
print(x)

x=[i*2 for i in tuple1]
print(x)

x=[i*2 for i in tuple1 if i==4]
print(x)

x=[i*3 for i in tuple1 if (i*3)<12]
print(x)

print("**Set comprehension**")
List1=[1,2,3,4,5]
x={i for i in List1}
print(x)

x={i*2 for in List1}
print(x)

x={i*2 for i in List1 if i==4}
print(x)

x={i*3 for i in List1 if (i*3)<12}
print(x)

print("**Dict  Comprehensions**")
List1={1,2,3,4,5}
x={i:i for i in List1}
print(x)

x={i:i*2 for i in List1}
print(x)

x={i:i*2 for i in List1 if i==4}
print(x)

x={i:i*3 for i in List1 if (i*3)<12}
print(x)


print("**Lambda")
print("** Lambda with function name")
akhil=lambda a: a+6
# same as def akhil(x)
#			  x+6
print(akhil(10))

akhil=lambda a,b: a+b
print(akhil(2,5))

akhil=lambda a,b,c: a+(2*b)+(3*c)
print(akhil(2,3,5))

print("**Lambda as anonymus(function name not given)")
print("see-how a value is 1?")
#example 1
def myfunc(n):
  return lambda a : a-n
mytripler = myfunc(15)
print(mytripler(1))

#example 2
def testfunc(num):
    return lambda x : x * num
result1 = testfunc(10)
print(result1(9))

print("**see-Lambda as anonymus with filter**")
numbers_list = [2, 6, 8, 11, 4, 12, 7, 13, 17, 0, 3, 21,10]
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
print(filtered_list)

print("**see-Lambda as anonymus with map**")
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)

## mapper ?? see

print("***Iterators")
print("***for on In built Iterators")
num=[7,8,9,5] 
for i in num:
	print (i)
''' list is inbuilt Iteraotr because we can use For..In Loop 
, iter() and __next__() on List.that's why List , Tuple , set,
 disctionary are inbuilt iterators
'''
print("***next on In built Iterator")
it=iter(num)
print(it.__next__())
print(it.__next__()) 

print("***to create custom iterator(on which we can use for..in,iter() and next function")
print("***custom iterator from scratch/ Not IMP")
class Topten:
	def __init__(self):
		self.num=50

	def __iter__(self):
		return self

	def __next__(self):
		if self.num <= 55:
			val=self.num
			self.num += 1
			return val
		else:
			raise StopIteration

values=iter(Topten())
print(values.__next__())
print(values.__next__())
print(values.__next__())

print("***Generator/custom Iterators with yield")
print("***For on custom Generator/iterator")
def akhil():
	yield 1
	yield 2
	yield 3
for i in akhil():
	print (i)

print("***next on custom Generator/iterate")
def palak():
	yield 'a'
	yield 'b'
	yield 'c' 
x=palak()
print(x.__next__())
print(x.__next__())

print("**Decorator**")
print("**if 2 names are equal their functions are equal")
def succ(x):
	return x + 1

successor = succ
successor(10)
succ(10)

'''
foo = our_decorator(foo)
same as 
@our_decorator
def foo()
'''
