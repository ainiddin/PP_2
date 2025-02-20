def even(n):
    for i in range(1,n+1):
        if i % 2==0:
            yield i

n=int(input("give n: "))
for x in even(n):
    print(x)