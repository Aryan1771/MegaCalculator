import math
run=True
pi=22/7
g=1/3
kol=1/2
print("Welcome to Shape calculator which helps in calculating CSA, TSA, Volume, Area, Perimeter of differnt shapes")
print("Choose 1 for 3-D Shapes")
print("Choose 2 for 2-D Shapes")
Shape=input("Choose type of shape \n")
if Shape=="1":
  print("Choose 1 for cube")
  print("Choose 2 for cuboid")
  print("Choose 3 for cone")
  print("Choose 4 for cylinder")
  print("Choose 5 for sphere")
  print("Choose 6 for hemisphere")
  a=input("Enter your choice \n")
  if a=="1":
    print("Choose 1 to find Volume")
    print("Choose 2 to find Total Surface Area")
    print("Choose 3 to find Curved Surface Area")
    d=input("Enter your choice \n")
    if d=="1":
      s=float(input("Enter the side \n"))
      v=s*s*s
      print("Volume = ", v)
    elif d=="2":
      s=float(input("Enter the side \n"))
      t=6*s*s
      print("Total Surface Area = ", t)
    elif d=="3":
      s=float(input("Enter the side \n"))
      c=4*s*s
      print("Curved Surface Area = ", c)
    else:
      print("Invalid input")
  elif a=="2":
    print("Choose 1 to find Volume")
    print("Choose 2 to find Total Surface Area")
    print("Choose 3 to find Curved Surface Area")
    d=input("Enter your choice \n")
    if d=="1":
      l=float(input("Enter length \n"))
      b=float(input("Enter breadth \n"))
      h=float(input("Enter height \n"))
      v=l*b*h
      print("Volume = ", v)
    elif d=="2":
      l=float(input("Enter length \n"))       
      b=float(input("Enter breadth \n"))
      h=float(input("Enter height \n"))
      t=2*((l*b)+(b*h)+(h*l))
      print("Total Surface Area = ", t)
    elif d=="3":
      l=float(input("Enter length \n"))
      b=float(input("Enter breadth \n"))
      h=float(input("Enter height \n"))
      c=2*h*(l+b)
      print("Curved Surface Area = ", c)
    else:
      print("Invalid input")
  elif a=="3":
    print("Choose 1 to find Volume")
    print("Choose 2 to find Total Surface Area")
    print("Choose 3 to find Curved Surface Area")
    d=input("Enter your choice \n")
    if d=="1":
      r=float(input("Enter radius \n"))
      h=float(input("Enter height \n"))
      v=pi*g*r*r*h
      print("Volume = ", v)
    elif d=="2":
      r=float(input("Enter radius \n"))
      h=float(input("Enter height \n"))
      l = math.sqrt((r*r )+ (h*h))
      t=(pi*r*r)+(pi*r*l)
      print("Total Surface Area = ", t)
    elif d=="3":
      r=float(input("Enter radius \n"))
      h=float(input("Enter height \n"))
      l = math.sqrt((r*r )+ (h*h))
      c=pi*r*l
      print("Curved Surface Area = ", c)
    else:
      print("invalid input")
  elif a=="4":
    print("Choose 1 to find Volume")
    print("Choose 2 to find Total Surface Area")
    print("Choose 3 to find Curved Surface Area")
    d=input("Enter your choice \n")
    if d=="1":
      r=float(input("Enter radius \n"))
      h=float(input("Enter height \n"))
      v=pi*r*r*h
      print("Volume = ", v)
    elif d=="2":
      r=float(input("Enter radius \n"))
      h=float(input("Enter height \n"))
      t=2*pi*r*(r+h)
      print("Total Surface Area = ", t)
    elif d=="3":
       r=float(input("Enter radius \n"))
       h=float(input("Enter height \n"))
       c=2*pi*r*h
       print("Curved Surface Area = ", c)
    else:
       print("invalid input")
  elif a=="5":
    print("Choose 1 to find Volume")
    print("Choose 2 to find Total Surface Area")
    d=input("Enter your choice \n")
    if d=="1":
       r=float(input("Enter radius \n"))
       v=pi*r*r*r*4*g
       print("Volume = ", v)
    elif d=="2":
       r=float(input("Enter radius \n"))
       t=4*pi*r*r
       print("Total Surface Area = ", t)
    else:
       print("nvalid input")
  elif a=="6":
    print("Choose 1 to find Volume")
    print("Choose 2 to find Total Surface Area")
    print("Choose 3 to find Curved Surface Area")
    d=input("Enter your choice \n")
    if d=="1":
       r=float(input("Enter radius \n"))
       v=pi*r*r*r*2*g
       print("Volume = ", v)
    elif d=="2":
       r=float(input("Enter radius \n"))
       t=3*pi*r*r
       print("Total Surface Area = ", t)
    elif d=="3":
       r=float(input("Enter radius \n"))
       c=2*pi*r*r
       print("Curved Surface Area = ", c)
    else:
       print("Invalid input")
  else:
     print("Invalid input")
elif Shape=="2":
  print("Choose 1 for square")
  print("Choose 2 for rectangle")
  print("Choose 3 for triangle")
  print("Choose 4 for circle")
  print("Choose 5 for semicircle")
  a=input("Enter your choice \n")
  if a=="1":
    print("Choose 1 to find area")
    print("Choose 2 to find perimeter")
    d=input("Enter your choice \n")
    if d=="1":
       s=float(input("Enter the side \n"))
       area=s*s
       print("Area = ", area)
    elif d=="2":
       s=float(input("Enter the side \n"))
       perimeter = 4*s
       print("Perimeter = ", perimeter)
  elif a=="2":
    print("Choose 1 to find area")
    print("Choose 2 to find perimeter")
    d=input("Enter your choice \n")
    if d=="1":
       l=float(input("Enter the length \n"))
       b=float(input("Enter the breadth \n"))
       area=l*b
       print("Area = ", area)
    elif d=="2":
       l=float(input("Enter the length \n"))
       b=float(input("Enter the breadth \n"))
       perimeter = 2*(l+b)
       print("Perimeter = ", perimeter)
  elif a=="3":
    print("Choose 1 to find area")
    print("Choose 2 to find perimeter")
    d=input("Enter your choice \n")
    if d=="1":
       b=float(input("Enter the base \n"))
       h=float(input("Enter the height \n"))
       area=b*h*kol
       print("Area = ", area)
    elif d=="2":
       s1=float(input("Enter first side \n"))
       s2=float(input("Enter second side \n"))
       s3=float(input("Enter third side \n"))
       perimeter = s1+s2+s3
       print("Perimeter = ", perimeter)
  elif a=="4":
    print("Choose 1 to find area")
    print("Choose 2 to find circumference")
    d=input("Enter your choice \n")
    if d=="1":
       r=float(input("Enter the radius \n"))
       area=pi*r*r
       print("Area = ", area)
    elif d=="2":
       r=float(input("Enter the radius \n"))
       circumference = 2*pi*r
       print("Circumference = ", circumference)
  elif a=="5":
    print("Choose 1 to find area")
    print("Choose 2 to find perimeter")
    d=input("Enter your choice \n")
    if d=="1":
       r=float(input("Enter the radius \n"))
       area=pi*r*r*kol
       print("Area = ", area)
    elif d=="2":
       r=float(input("Enter the radius \n"))
       circumference=2*pi*r
       print("Circumference = ", circumference)
  else:
    print("Invalid input")
else:
  print("Invalid input")