import re
with open(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab5\row.txt","r") as f:
    file1 = f.read()
file="There Are Several Geese In The Pond"
pattern="[A-Z][a-z]*"
match=re.findall(pattern,file)
print(match)