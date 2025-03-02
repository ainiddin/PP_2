import re
with open(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab5\row.txt","r") as f:
    file=f.read()
pattern="ab*"
match=re.findall(pattern,file)
print(match)