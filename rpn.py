#!/usr/bin/env python3 #

def calculate(myarg):
	stack = list()
	for token in myarg.split():
		if token == '+':	
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 + arg2
			stack.append(result)
		elif token == '-':
			arg1 = stack.pop()
			arg2 = stack.pop()
			result = arg1 - arg2
			stack.append(result)

		else:
			stack.append(token)
	print(stack)

def main():
	while True:
		calculate(input("rpm calc> "))

if __name__ == '__main__':
	main()
