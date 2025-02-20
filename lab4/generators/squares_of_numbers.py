def gen(N):
    for i in range(N):
        yield i**2
N=int(input("give any number:"))
for x in gen(N):
    print(x)