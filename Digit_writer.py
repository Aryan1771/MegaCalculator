b=a=int(input("Enter a number whose parts will be displayed starting from ones unit place \n"))
#Version one
if a<=0:
    print("Enter higher number")
else:
    while a%10 >0:
        print(a%10, end=" ")
        a= a//10

#Version two
Lis=[]
if b<=0:
    print("Enter higher number")
else:
    while b%10 >0:
        Lis.append(b%10)
        b= b//10
print(Lis[::-1])