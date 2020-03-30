a,b,c='fff',10,10.25
print('%s,%g,%f' %(a,b,c))

print('{1},{0},{2}' .format(a,b,c))

print(type(a))

def aki(x,y='bb',z='cc'):
	print('hi',x,y,z)

aki('aa')

def a(*v):
	print(v)

a(1,2,3,4,5,6,7)

aki('gggg')

print(a)


# inside function - same variable can not use as local and global var
def aki2(x):
	#av=123
	global av
	av=456
	

aki2('dd')
print(av)