import re
with open(r"C:\Users\esirk\Desktop\study\PP_2\vscode\lab1\lab5\row.txt","r") as f:
    file1=f.read()
file="the_snake_case_inscription"
pattern="_([a-z])"
match=re.findall(pattern,file)
for a in match:
    file=file.replace(f"_{a}",a.upper())
print(file)