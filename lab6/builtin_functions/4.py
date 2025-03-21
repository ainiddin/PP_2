import math 
import time
def fun_root(a):
    c=math.sqrt(a)
    return c
a=int(input("give a number: "))
b=int(input("give a miliseconds: "))
time.sleep(b/1000)
print(f"Square root of {a} after {b} miliseconds is {fun_root(a)}")