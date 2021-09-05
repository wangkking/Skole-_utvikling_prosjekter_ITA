#Addere og Multiplisere

#Legger sammen to tall
def adder():
    tall_1=int(input("legg til et tall:  "))
    tall_2=int(input("legg til et nytt tall:  "))
    sum = (tall_1+tall_2)
    print ("Summen av", tall_1, "og", tall_2, "er",  sum, "\n")

#Multpleserer to tall
def multiple():
    tall_1=int(input("legg til et tall:  "))
    tall_2=int(input("legg til et nytt tall:  "))
    produkt = (tall_1*tall_2)
    print ("produkte av", tall_1, "og", tall_2, "er",  produkt, "\n")

print("Hva vil du gjøre? \n 1 -Addere \n 2 -Multiplisere \n 3-Ingen ting ")



valg = input("Ditt valg: ")

if valg=="1":
    adder()

elif valg=="2":
    multiple()

else:
    print("exit")
