#this program counts the individual words in a string and prints the number of words.
usrstr = input('I am going to need a string of words please: ')
count = 1
for i in usrstr:
	if i == ' ':
		count +=1
print (count)
