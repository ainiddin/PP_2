dic={
    "owner1":{
    "бренд" : "Айфон",
    "поколение" : "14",
    "тип" : "прошка",
    "год":"2024"
    },
    "owner2":{
    "бренд" : "редми",
    "поколение" : "13",
    "тип" : "ноут",
    "год":"2024"
    },
    "owner3":{
    "бренд" : "самсунг",
    "поколение" : "эс 24",
    "тип" : "ультра",
    "год":"2024"
    }
}
print(dic)

#create several dics and join them into one 
student1={
    "year":"first",
    "major":"IS"
}
student2={
    "year":"third",
    "major":"OGP"
}
student3={
    "year":"second",
    "major":"pedagogue"   
}
base={
    "student1":student1,
    "student2":student2,
    "student3":student3,
}
for a,b in base.items():
    print(a + " :","\n")
    for c in b:
        print(c + " : " + b[c])
    print("\n")