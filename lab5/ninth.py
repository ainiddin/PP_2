import re
with open(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab5\row.txt","r") as f:
    file1=f.read()
file="ThereAreSeveralGeeseInThePond"
pattern="[A-Z][a-z]*"
match=re.findall(pattern,file)
a=""
for i in match:
    a=a+(i)
    a+=" "
print(a)