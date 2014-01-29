#this is a calculator.
operators = ['Addition = 1', 'Subtraction = 2', 'Multiplication = 3', 'Division = 4']
for i in operators:
	print (i)

while True:
		try:
			usrop = int(input('Please choose an operator above using its numerical identifier: '))
			if usrop in (1,2,3,4):
				break
			else:
				print('Invalid Number!')
		except ValueError:
			print ('That was not even a number!')
			
while True:
	try:
		firstn = float(input('Enter your first number: '))
		secondn = float(input('Enter your second number: '))
		break
	except ValueError:
		print ('That was not a number!')

if usrop == 1:
	print (firstn + secondn)
elif usrop == 2:
	print (firstn - secondn)
elif usrop == 3:
	print (firstn * secondn)
elif usrop == 4:
	print (firstn / secondn)
