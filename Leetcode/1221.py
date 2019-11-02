S="LLRRLLRRLLRR"

	#print (S[x])
a=1
if S[0]=="L":
	for x in range(len(S)):
		print(S[x])
		if S[x]=="R":
			if S[x]=="L":
				a=a+1
				print(a)

	


