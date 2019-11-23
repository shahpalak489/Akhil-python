dictionary=["albums","barely","befoul","convex","hereby","jigsaw","tailor","weaver"]

pieces=["al","bums","bar","ely","be","foul","con","vex","here","by","jig","saw","tail","or","we","aver"]

for i in range(len(pieces)):
	for j in range(len(pieces)):
		if (pieces[i]!=pieces[j]):
			word=(pieces[i]+pieces[j])
			for k in range(0,8):
				if (word==dictionary[k]):
					print(word)
				else:
					print(word+"!="+dictionary[k])

