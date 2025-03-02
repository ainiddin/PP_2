import re
file="TheCamelCaseInscription"
pattern="([a-z])([A-Z])"
replacement=r"\1_\2"
match=re.sub(pattern,replacement,file)
print(match)