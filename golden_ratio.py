import math
#fibo
def fib(n):
    if (n <= 1):
        return n
    else:
        return (fib(n - 1) + fib(n - 2))

n = 10
#gold
for x in range(n):
    print("Fibbonaci: " , fib(n - 1) + fib(n - 2))
    print("Golden Ratio:", fib(n - 1) / fib(n - 2))

#fibb 2nd divided by 1st, 1.619
print("python golden ratio:")
print((math.sqrt(5)-1)/2)