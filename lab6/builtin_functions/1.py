a = input("list: ")
b = list(map(int, a.split()))#here we have list and map builtin function 
c=1
for i in b:
    c*=i
print(f"The multiplication of all numbers in list is equal to {c}")#and here print is also builtin function