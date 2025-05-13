import math
print("Welcome to the best trignometric calculator")
print("Enter 1 if you have angle θ")
print("Enter 2 if you have P,B,H")
a = input("Enter your choice \n")
if a == "1":
    print("Press 1 to take out sinθ")
    print("Press 2 to take out cosθ")
    print("Press 3 to take out tanθ")
    print("Press 4 to take out cosecθ")
    print("Press 5 to take out secθ")
    print("Press 6 to take out cotθ")
    a2 = input("Enter your choice \n")
    θ = float(input("Enter the angle θ ? \n"))
    if a2 == "1":
        print(math.sin(θ))
    elif a2 == "2":
        print(math.cos(θ))
    elif a2 == "3":
        print(math.tan(θ))
    elif a2 == "4":
        θ1 = math.sin(θ)
        print(1/θ1)
    elif a2 == "5":
        θ2 = math.cos(θ)
        print(1/θ2)
    elif a2 == "6":
        θ3 = math.tan(θ)
        print(1/θ3)
    else:
        print("Invalid input")
elif a == "2":
    print("Press 1 to take out sinθ")
    print("Press 2 to take out cosθ")
    print("Press 3 to take out tanθ")
    print("Press 4 to take out cosecθ")
    print("Press 5 to take out secθ")
    print("Press 6 to take out cotθ")
    a3 = input("Enter your choice \n")
    if a3 == "1":
        p=float(input("Enter the perpendicular \n"))
        h=float(input("Enter the hypotenouse \n"))
        print(p/h)
    elif a3 == "2":
        b=float(input("Enter the base \n"))
        h=float(input("Enter the hypotenouse \n"))
        print(b/h)
    elif a3 == "3":
        p=float(input("Enter the perpendicular \n"))
        b=float(input("Enter the base \n"))
        print(p/b)
    elif a3 == "4":
        p=float(input("Enter the perpendicular \n"))
        h=float(input("Enter the hypotenouse \n"))
        print(h/p)
    elif a3 == "5":
        b=float(input("Enter the base \n"))
        h=float(input("Enter the hypotenouse \n"))
        print(h/b)
    elif a3 == "6":
        p=float(input("Enter the perpendicular \n"))
        b=float(input("Enter the base \n"))
        print(b/p)
    else:
        print("Invalid input")