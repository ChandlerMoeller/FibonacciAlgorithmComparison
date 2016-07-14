FibCounter = 0
DynamicFibCounter = 0
Table = {}
OptDynamicFibCounter = 0
OptDynamicFibCache = 0


def Fibonacci(value):
	global FibCounter

	if value is 1:
		return 1
	elif value is 0:
		return 0
	else:
		FibCounter += 1

		return(Fibonacci(value-1) + Fibonacci(value-2))

def DynamicFibonacci(value):
	global DynamicFibCounter
	global Table

	if value is 1:
		return 1
	elif value is 0:
		return 0
	else:
		if value in Table:
			return(Table[value])
		else:
			DynamicFibCounter += 1

			returnval = DynamicFibonacci(value-1) + DynamicFibonacci(value-2)
			Table[value] = returnval
			return(returnval)

def OptDynamicFibonacciinit(value):
	global OptDynamicFibCounter
	global OptDynamicFibCache

	if value is 1:
		OptDynamicFibCache = 1
		return 1
	elif value is 0:
		OptDynamicFibCache = 0
		return 0
	else:
		OptDynamicFibCounter += 1

		return(OptDynamicFibonacci(value-1))

def OptDynamicFibonacci(value):
	global OptDynamicFibCounter
	global OptDynamicFibCache

	if value is 1:
		OptDynamicFibCache = 1
		return 1
	else:
		OptDynamicFibCounter += 1
		
		tmp = OptDynamicFibonacci(value-1)
		returnval = tmp + OptDynamicFibCache
		OptDynamicFibCache = tmp
		return(returnval)

print("Welcome to Fibonacci")
print("This program will find the value of the of Fibonacci Sequence at the position input")
value = raw_input("Please input the position desired:\n")
value = int(value)

print("")
print("Fibonacci value is: %d" %(Fibonacci(value)))
print("Recursions used: %d" %(FibCounter))

print("")
print("Dynamic: Fibonacci value is: %d" %(DynamicFibonacci(value)))
print("Dynamic: Recursions used: %d" %(DynamicFibCounter))
print("Dynamic: Cache Size: %d" %(len(Table)))

print("")
print("OptDynamic: Fibonacci value is: %d" %(OptDynamicFibonacciinit(value)))
print("OptDynamic: Recursions used: %d" %(OptDynamicFibCounter))
print("OptDynamic: Cache Size: 2")

