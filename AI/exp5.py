n=input("Enter the sentence:")
print("number of character:")
print("uppercase:",n.upper())
print("lowercase:",n.lower())
print("with underscore:",n.replace("","_"))
if "python" in n:
	print("The word python is in the sentence:")
else:
	print("The word python is not in thesentence")
