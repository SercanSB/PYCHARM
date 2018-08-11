sınıfListesi={"mustafa":215 , "ahmet":597, "alkan":561 }
print(sınıfListesi)


sınıfListesi["Sercan"]=2015
print(sınıfListesi)


del sınıfListesi["ahmet"]
print(sınıfListesi)


print(sınıfListesi.keys())

print(sınıfListesi.values())


###########################################################


sınıfListesi1=["musa","sezen","ayşe"]
print("musa" in sınıfListesi1)

sözlük={"musa":1,"sezen":2,"ayşe":3}
print("sezen" in sözlük)

print(1 is "musa" in sözlük)