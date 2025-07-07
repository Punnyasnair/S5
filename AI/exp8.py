def cal(a,b,c):
	match c:
		case 1:
			return a+b
		case 2:
			return a-b
		case 3:
			return a*b
		case 4:
			return a/b
		case _:
			return ("Invalid")
		
		
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Operations:\n1. Addition\n2.Subtraction\n3.Multiplication\n4.Division\nChoose a number: "))
d = cal(a,b,c)
print(d)
