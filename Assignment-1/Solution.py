# Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one number and returns the factorial of given number.

# This function takes in one number and returns one number.


def factorial(n):
	'''
	n is positive Integer
	
	returns: a positive integer, the factorial of n.
	'''
	# Your code here
	val = 1
	for i in range(1,n+1):
		val = val*i
	return val

def main():
	data=input()
	for i in range(int(data)):
		a = input()
		print(factorial(int(a)))	

if __name__== "__main__":
	main()