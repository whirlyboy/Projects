#this program takes a word and translates it to Pig Latin!
pyg = 'ay'

word = input('Enter your word to be translated: ')
first = word[0]

if first not in 'aeiou':
	print (word[1::] + '-' + first + pyg)
else:
	print (word + pyg)
