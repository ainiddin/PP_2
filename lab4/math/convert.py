import math
def radian():
    degree=int(input("give degree : "))
    radian=degree*math.pi/180
    radian=math.radians(degree)
    return radian

print(radian())