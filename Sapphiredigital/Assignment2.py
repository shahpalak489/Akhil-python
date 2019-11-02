str= "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
#str1= "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"

def is_palin(s):
	return s == s[::-1]

def longestPalindrome(s):
	longest_str =''
	for i in range(len(s)):
		#print(i)
		for j in range(len(s),i,-1):
			#print(j)
			sub_str= s[i:j]
			#print(sub_str)
			if is_palin(sub_str) and len(longest_str) < len(sub_str):
				longest_str = sub_str

	print(longest_str)
	return(longest_str)

longestPalindrome(str)




'''
str1= "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
str= "abcbh"

def is_palin(s):
	return s == s[::-1] # check mirror image 

def longestPalindrome(s):
	longest_str =''
	for i in range(len(s)):
		#print(i) (0,1,2,3)
		for j in range(len(s),i,-1):    
			#print(j) (4,0,-1) = (4,3,2,1)
			sub_str= s[i:j] # = (0,4),(0,3),(0,2),(0,1),(1,4),(1,3),(1,2),(2,4),(2,3),(3,4)
			#print(sub_str)
			#print(is_palin(sub_str))
			#print(is_palin(sub_str) and len(longest_str))
			if is_palin(sub_str) and len(longest_str) < len(sub_str):
				longest_str = sub_str

	print(longest_str)
	return(longest_str)
 
longestPalindrome(str) '''
