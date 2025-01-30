dic1={
    "бренд" : "Айфон",
    "поколение" : "14",
    "тип" : "прошка",
    "год":"2024"
}
print(dic1)

#if we write one item and then write the same item and give him another value its value will be the last one
dic1={
    "бренд" : "Айфон",
    "поколение" : "14",
    "тип" : "прошка",
    "год":"2024",
    "год":"2023"
}
print(dic1["год"])

#in order to add new key to dic1 we just write new key and equalize it to value we need
dic1={
    "бренд" : "Айфон",
    "поколение" : "14",
    "тип" : "прошка",
    "год":"2024"
}
print(dic1)
dic1["owner"]="Ainiddin"
print (dic1)

#to get only one side of dic1 we use this two commands :dic1.keys() , dic1.values()
dic1={
    "бренд" : "Айфон",
    "поколение" : "14",
    "тип" : "прошка",
    "год":"2024"
}
print(dic1.keys())
print(dic1.values())

#print all keys and values from dic1 one by one by using loop
dic1={
    "бренд" : "Айфон",
    "поколение" : "14",
    "тип" : "прошка",
    "год":"2024"
}
for i in dic1:
    print(i)
    print(dic1[i])
for a, b in dic1.items():
    print(a,b)

#copy dic1 by command copy
dic1={
    "бренд" : "Айфон",
    "поколение" : "14",
    "тип" : "прошка",
    "год":"2024"
}
dic2=dic1.copy()
#or
dic2=dict(dic1)
print(dic2)
