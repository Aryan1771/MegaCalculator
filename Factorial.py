def Factorial():
  hev=float(input("Enter the number you want to make a factorial of: \n"))
  i=1
  t=1
  while i <= hev:
    t*=i
    i+=1
  print("Factorial = ", t)
Factorial()