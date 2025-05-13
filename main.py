def multiply(x,y):
    return x*y
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def divide(x,y):
    return x/y
def floor_division(x,y):
    return x//y
print("WELCOME TO WORLDS MOST INTELLIGENT AND POWERFUL CALCULATOR Created by Aryboss")
run=True
while run:
    print("Press 1 for operations")
    print("Press 2 for extra operations")
    print("Press 3 for table maker")
    print("Press 4 for prime number writer")
    print("Press 5 for trignometric calculator")
    print("Press 6 for temperature convertor")
    print("Press 7 for shape calculator")
    print("Press 8 to exit")
    choose=input("Choose an option \n")
    if choose=="1": 
        print("Press 1 to add")
        print("Press 2 to subtract")
        print("Press 3 to multiply")
        print("Press 4 to divide")
        choice=input("Choose an operation \n")
        num1=float(input("Choose first number \n"))
        num2=float(input("Choose second number \n"))
        if choice=="1":
            print(num1, " + ", num2, " = ", add(num1,num2)) 
        elif choice=="2":
            print(num1, " - ", num2, " = ", subtract(num1,num2))
        elif choice=="3":
            print(num1, " * ", num2, " = ", multiply(num1,num2))
        elif choice=="4":
            print(num1, " ÷ ", num2, " = ", divide(num1,num2))
        else:
            print("Invalid input")
    elif choose=="2":
        print("Press 1 to square")
        print("Press 2 to cube")
        print("Press 3 to floor calculate")
        print("Press 4 for pi calculator")
        print("Press 5 for Binomial Calculator")
        print("Press 6 for Euler's number Calculator")
        print("Press 7 for Fibonacci Series")
        print("Press 8 for Digit writer")
        print("Press 9 for Factorial")
        h=input("Choose the extra operation \n")
        if h=="1":
            j=0
            num=float(input("Choose a number to square \n"))
            i=float(input("Choose how many times to square the number \n"))
            while j<=i:
              h = num**j
              print(j, " => ", h)
              j+=1
        elif h=="2":
            a=0
            numa=float(input("Choose a number to cube \n"))
            b=float(input("Choose how many times to cube \n"))
            while a<=b:
              l = numa**a
              print(a, " => ", l)
              a+=1
        elif h=="3":
            num1=float(input("Choose first number \n"))
            num2=float(input("Choose second number \n"))
            print(num1, " // ", num2, " = ", floor_division(num1,num2))
        elif h=="4":
            import Pi_Calculator as Pi
        elif h=="5":
            import Binomial_Calculator as Bi
        elif h=="6":
            import Eulers_number_Calculator as E
        elif h=="7":
            import Fibonacci as Fibo
        elif h=="8":
            import Digit_writer as Digi
        elif h=="9":
            import Factorial as Fact
    elif choose=="3":
          print("Welcome to Table maker")
          Table=float(input("Which number do you want a table for ? \n"))
          n=1
          while n<11:
            a = Table*n
            print(Table, " X ", n, " = ", a)
            n += 1
    elif choose =="4":
        from Prime_Number_Calculator import PrimeNumber as P
    elif choose =="5":
        import Trignometric_Calculator as T
        pass
    elif choose =="6":
        import Temperature_Convertor as C
    elif choose =="7":
        import Shape_Calculator as S
    elif choose=="8":
        print("THANK YOU FOR WORKING WITH US")
        print("Exiting.......")
        run=False
        exit()
    else:
        print("Invalid input")
def l():
    P()
    T()
    C()
    S()
    Pi()
    Bi()
    E()
    Fibo()
    Digi()
    Fact()
    pass