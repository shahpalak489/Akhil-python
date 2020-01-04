print("first 10 numbers")
for x in range(10):
	print(x)

print(" 10 numbers with 3 increment")
for x in range(2,10,3):
	print(x)

print("first 10 odd numbers")
for x in range(10):
	if x%2 == 0:
		print(x)

''' IMP
just to arrange by asc or desc ---> sort
to arrange with any other logic ---> sorted
'''
print("arrange in asc order")
a=[1,4,5,3,2]
a.sort()
print(a)

b=['a','e','b','d','c']
b.sort()
print(b)

print("arrange in desc order")
e=[1,4,5,3,2]
e.sort(reverse=True)
print(e)

f=['a','e','b','d','c']
f.sort(reverse=True)
print(f)

print("arrange given list by length")
i=['bcde','cd','def','a']
j=sorted(i,key=len)
print(j)

print("arraneg by function")
def func(x): 
    return x % 7
L = [15, 3, 11, 7] 
m = sorted(L, key = func)
print(m)






