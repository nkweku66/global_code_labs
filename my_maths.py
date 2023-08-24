operation = (input("Do you want to add, subtract, multiply or divide?\n")).lower()
x = int(input("First value:"))
y = int(input("Second value:"))

def calculate(operation, x, y):	
	if(operation == 'add'):
		print(x + y)
	elif(operation == 'subtract'):
		print(x - y)
	elif(operation == 'multiply'):
		print(x * y)
	elif(operation == 'divide'):
		print(x / y)

calculate(operation, x, y)
