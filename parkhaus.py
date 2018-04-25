        #parkhaus.py 
        # Angabe für das Beispiel_ siehe Moodle

print ("Linienbus-Simulator")

Personen = 0 

haltestellen = input("Wie viele Haltstellen gibt es? ")

Haltstellen = int(haltestellen)

for h in range (0,10):

        einsteiger = int(input("Wie viele Personen steigen ein? "))
        aussteiger = int(input("Wie viele Personen steigen aus? "))
        

        print("Es gibt ",haltestellen," Haltestellen")

        print("Es steigen " ,einsteiger, "Personen ein") 

        print("Es steigen " ,aussteiger, "Personen aus") 
        if(Personen+einsteiger > 60):
            print ("Es können", Personen + einsteiger  - 60,"nicht einsteigen")
            Personen = 60
            Personen=Personen-aussteiger

        elif (Personen+einsteiger-aussteiger < 0):
            print("Es müssen mindestens 0 Personen im Bus sein") 
            Personen = 0
            Personen = Personen + einsteiger
        else:
            Personen = Personen + einsteiger
            Personen= Personen - aussteiger
        
            
        print("Zurzeit sind ",Personen,"Personen im Bus")     


   





