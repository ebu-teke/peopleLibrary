import os
import json
os.chdir(os.getcwd()+"/pastones/userdatas")
def addUser(name,surname,age,hobbies):
    with open("wholeroomofmankind.json","r",encoding="utf-8") as file:
        people = json.load(file)
    newone = {
        "firstName": name,
        "lastName": surname,
        "age": age,
        "hobbie": hobbies
    }
    people.append(newone)
    with open("wholeroomofmankind.json","w",encoding="utf-8") as file:
        json.dump(people,file,ensure_ascii=False,indent=2)
def deleteUser(name,surname):
    with open("wholeroomofmankind.json","r",encoding="utf-8") as file:
        people = json.load(file)
    i=0
    for x in people:
        if(x["firstName"] == name and x["lastName"]==surname):
            people.pop(i)
        else:
            i+=1
    with open("wholeroomofmankind.json","w",encoding="utf-8") as file:
        json.dump(people,file,ensure_ascii=False,indent=2)
def listUsers():
    with open("wholeroomofmankind.json","r",encoding="utf-8") as file:
        people = json.load(file)
    print("--------------------")
    for x in people:
        print(x["firstName"]+" "+x["lastName"])
        print(str(x["age"])+" yaşında.")
        print("Favori hobisi: "+x["hobbie"])
        print("--------------------")
while True:
    print("""
    *************************
    1 - Kişi Ekle
    2 - Kişi Sil
    3 - Kişileri listele
    4 - Programı sonlandır
    *************************""")
    try:
        islem = int(input("İşlem numrası: "))
    except:
        print("Geçersiz.")
        continue
    if(islem==1):
        a = input("Kişinin ismini yazın: ")
        b = input("Kişinin soyismini yazın.")
        try:
            c = int(input("Kişinin yaşını girin:"))
        except:
            print("Yaş geçersiz.")
        d = input("Kişinin favori hobisini girin.")
        addUser(a,b,c,d)
        print("Kişi eklendi.")
    elif(islem==2):
        e = input("Kişinin ismini yazın: ")
        f = input("Kişinin soyismini yazın.")
        deleteUser(e,f)
        print("Kişi silindi.")
    elif(islem==3):
        listUsers()
    elif(islem==4):
        print("Program sonlandırıldı.")
        break
    else:
        print("Geçersiz.")
        

