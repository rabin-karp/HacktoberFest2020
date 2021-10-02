# provide input a and b in same diff lines
''' Ex :
	1 
	2 
'''
#using try, except else will help you avoid errors
try:
	a = int(input('Enter the First Number For Multiplication : ')) #ask for the specified input
	b = int(input('Enter the Second Number For Multiplication : ')) 
except:
	print('Invalid Input')
else:
	c = a * b
	print(c)
