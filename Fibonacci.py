#Fibonacci calculator
print("Welcome to Fibonacci number writer")
n = int(input("Enter the number of times you want fibonacci series \n"))
num1, num2= 0, 1
sumn=0
if n <= 0 :
    print("Number is less write a higher number")
else:
    for i in range(1,n+1):
      print(sumn, end=" ")
      num1=num2
      num2=sumn
      sumn=num1+num2
