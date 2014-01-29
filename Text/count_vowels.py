#this program takes a user submitted string and counts the number of vowels in that string.
print ('Please enter a string so that I can count the vowels in it!')
usrtext = input('Your word, please: ')

count = 0
for i in usrtext:
	if i in 'aeiou':
		count += 1
print (count)
