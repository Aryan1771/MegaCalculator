print("Welcome to temperature convertor")
print("Choose 1 to convert fahrenheit to celsius")
print("Choose 2 to convert kelvin to celsius")
print("Choose 3 to convert fahrenheit to kelvin")
print("Choose 4 to convert kelvin to fahrenheit")
print("Choose 5 to convert celsius to kelvin")
print("Choose 6 to convert celsius to fahrenheit")
t = input("Choose the conversion method \n")
if t == "1":
  f1 = float(input("Enter temprature in fahrenheit \n"))
  C= (f1-32)*5/9
  print(C)
elif t=="2":
  k1 = float(input("Enter temprature in kelvin \n"))
  C= k1-273
  print(C)
elif t=="3":
  f2 = float(input("Enter temprature in fahrenheit \n"))
  C = (f2-32)*5/9
  K = C+273
  print(K)
elif t=="4":
  k2 = float(input("Enter temprature in kelvin \n"))
  C = k2-273
  F = C*9/5+32
  print(F)
elif t=="5":
  c1 = float(input("Enter temprature in celsius \n"))
  K = c1+273
  print(K)
elif t=="6":
  c2 = float(input("Enter temprature in celsius \n"))
  F = c2*9/5+32
  print(F)
else:
  print("Invalid input")