# This is a small code for binomial theorum
def Binomial_Calculator():
  run=True
  while run:
   print("This is a calculator for binomial theorum in the form (1+x)^n where n is whole number")
   print("Enter value of n as -0.1 to exit")
   x=float(input("Enter the number to put in x position of binomial theorum \n"))
   n=float(input("Enter the power of binomial expression n \n"))
   if n== -0.1:
       run=False
   i=0
   j=0
   t=1
   k=1
   S=0
   w=0
   for i in range(101):
       while j<=i:
           if j!=0:
               t*=j
           j+=1
       while w in range (i):
           v=n-w
           k*=v
           w+=1
       f=k/t
       l=x**i
       r=(f)*(l)
       S+=r
       i+=1
   print("(1+x)^n = ", S)
Binomial_Calculator()