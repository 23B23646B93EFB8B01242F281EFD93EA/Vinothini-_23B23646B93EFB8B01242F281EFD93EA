n= int(input("enter a number:"))
factorial=1
if n<0:
	print("factorial doesn't exit for negative number:")
elif n<0:
	print("factorial of 0 is 1 ")
else:
	for i in range(1,n+1):
		factorial=factorial * i
print("factorial:",factorial) 
	