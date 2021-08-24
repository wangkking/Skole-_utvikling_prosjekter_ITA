
høyden=int(input("Skriv høyden: "))
bredden=int(input("skriv bredden: ")+ "\n")

areal = høyden*bredden
omkrets= høyden*2+bredden+2

print("Areale er på objekte: " + str(areal))
print("Omkrestsen til objekte er: " + str(omkrets)+"\n")

#regne ut areal en trekant

grunlinje = int(input("Grunlinje: "))
høydde = int(input("Høydde: ")+"\n")

areal = høydde*grunlinje/2

print ("Arealet til trekanten var: " + str(areal))