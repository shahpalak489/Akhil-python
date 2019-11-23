 
def text2int(textnum,numwords={}):
	if not numwords:
		units = [
		"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
		"fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
		]
		
		tens = [ "","", "twenty", "thirty", "forty", "fifty", "sixty","seventy", "eighty", "ninety"]

		scales = ["hundred", "thousand", "million","billion","trillion"]

		#numwords["and"]=(1,0)
		for idx,word in enumerate(units):numwords[word] =(1,idx)
		for idx,word in enumerate(tens):
			numwords[word] = (1,idx*10)
			# print(numwords)

		for idx,word in enumerate(scales): numwords[word] = (10 **(idx * 3 or 2),0)


		current = result = 0
		for word in textnum.split():
			scale, increment = numwords[word]
			print("****")
			print(scale)
			print(increment)
			current=current * scale + increment #1/50, 1000,0
			print("abswer")
			print(current) #50, 50000
			if scale > 100:
				result = result + current #50000
				current=0

		return result+current
		
print(text2int("fifty thousand five hundred sixty one"))