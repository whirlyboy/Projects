#this code takes a user submitted string and checks if it's a palindrome, such as 'racecar'
usrpal = input('Go ahead, test my knowledge, see if I can tell a palindrome! Enter one here: ')
if usrpal == usrpal[::-1]:
	print('Yep, that sure is a palindrome alright')
else:
	print('nu-uh! Not a palindrome!')
