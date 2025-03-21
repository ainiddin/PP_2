a = input("list: ")
up = sum([1 for b in a if b.isupper()])
c=1
down= sum([c for b in a if b.islower()]) 
print(f"there are {up} uppercase letters")
print(f"there are {down} lowercases letters")