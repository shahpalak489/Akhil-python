
	# elif s[x]=="(":
	# 	a+= 1
	# 	print(a)
	# elif s[x]==")":
	# 	b+= 1
	# 	print(b)
	# elif a==b:
	# 	s=s.replace(")","")
	# else:import pdb
s="()()"
a=0
b=0
x=0

for x in range(len(s)):
	pdb.set_trace()
	print(s[x])
	print(x)
	if x==0:
		print(s)
		s=s.replace(s[0],"")
		print(s)
		continue
	# 	print("error")
'''
def space():
	s="()()()"
	a=0
	b=0
	for x in s:
	    if x=="(":
	        a+=1
	    elif x==")":
	        b+=1
	    else:
	        continue
	    print(a)
	    print(b)
	    print(x)
	    if a==b:
	    	s=s.replace(")(","")
	    	return(s)
space()
'''