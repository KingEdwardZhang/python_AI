#neez duts
import math
numyears= 2000
mum= range(1,numyears+1)
apr=1.0/numyears
sum1=1.0
for y in range(1,2000):
    sum1*=(1+apr)
    print("After year %d sum1 from for loop is %f" %(y,sum1))

print("math.e = %f"%math.e)