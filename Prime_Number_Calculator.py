def PrimeNumber():
 times = int(input("Number of prime numbers to print after 31 \n"))
 i = 0
 num = 11
 Lis1=[2,3,5,7,11,13,17,19,23,29,31]
 while i < times:
     num+=2
     if num%2 != 0 and num%3 != 0 and num%5 != 0 and num%7 != 0 and num%11 != 0 and num%13 != 0 and num%17 != 0 and num%19 != 0 and num%23 != 0 and num%29 != 0 and num%31!=0:
       Lis1.append(num)
       i+=1
     else:
         pass
 print(Lis1)
 print("Total number of prime numbers = ", len(Lis1))
PrimeNumber()