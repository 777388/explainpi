from decimal import Decimal
from decimal import getcontext
import sys
def pi(precision):
    getcontext().prec=precision
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) -
         Decimal(2)/(8*k+4) -
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range(precision))
pin = pi(int(sys.argv[1])*2)
x = []
for i in str(pin):
    if i == ".":
        continue
    else:
        x.append(i)
z = 13
d = 0
b = 0
try:
    for c in str(pin):
        print(str(int(z)+int(d))+" => "+str(x[b])+str(x[b+1]))
        d += 1
        b += 2
except:
    pass
