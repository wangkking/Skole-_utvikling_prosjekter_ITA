import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

while True:

    print("Hei jeg er en chatbot \nHva lurer du på? :\n 1. Hva heter jeg? :\n 2. Hvor gammel er jeg? :\n3. Hva er hobbne mine \n4. Hva slags teknologier har jeg brukt?")
    
    valg = int(input("Ditt nr: "))


    if valg == 1:
        print ("Mitt navn er Wang\nHelle navnet mitt er Wang King Son")
        

    elif valg == 2:
        print ("Jeg er 17 år og har b-dag 3 feb.")
        

    elif valg == 3: 
        print ("""Mine hobbyer er. 
    snowboard
    Fpv drone flyving 
    og litt programering""")
        

    elif valg == 4:
        print ("Jeg har drevel litt med arduino og c++ og litt html css og python.")
        
        
    else:
        print("forvel")
        break
    
    