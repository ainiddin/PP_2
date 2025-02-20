def gen(a,b):
    for i in range(a,b):
        yield i**2
a=int(input("give a:"))
b=int(input("give b:"))
for x in gen(a,b):
    print(x)
