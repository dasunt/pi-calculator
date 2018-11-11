from decimal import *

print("====================================================")
print("pi calculator using Bailey-Bowein-Plouffe formula")
print("====================================================")
print("\n")

plcs = input("Number of decimal places you are calculating pi to?  ")
i = input("Number of iterations?  ")

print("\nCalculating... \n\n")
getcontext().prec = int(plcs)+1


def plouffBig(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1))-(Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
    return pi


print (plouffBig(int(i)))
