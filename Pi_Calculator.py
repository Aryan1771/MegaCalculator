#1
pi=0.0
for i in range(1,10000000,4):
       pi+=4/i
       pi-= 4/(i+2)
print("Method 1",pi)
#2
import random
in_square = in_circle = pi2 = 0
for i in range(10000000):
    x = random.random()
    y = random.random()
    dist_= (x*x + y*y) ** 0.5
    in_square+=1
    if dist_ <= 1.0:
        in_circle+=1
pi2 = 4 * in_circle/ in_square
print("Method 2",pi2)