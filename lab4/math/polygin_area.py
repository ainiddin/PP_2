import math
def area():
    n=int(input("How many sides on your regular polygin : "))
    a=float(input("Give length of sides : "))
    S=(n*a**2)/(math.tan(math.radians(180/n))*4)
    return S
print("area:",area())