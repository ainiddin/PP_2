def to(N):
    for i in range(N,0-1,-1):
            yield i
N=int(input("give N: "))
for x in to(N):
    print(x)