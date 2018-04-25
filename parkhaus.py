        #parkhaus.py 
        # Angabe für das Beispiel_ siehe Moodle

print ("Linienbus-Simulator")

Personen = 0 

haltestellen = input("Wie viele Haltstellen gibt es? ")

Haltstellen = int(haltestellen)

for h in range (0,10):

        einsteiger = input("Wie viele Personen steigen ein ")

        Personen = Personen + int(einsteiger)

        print("Es gibt ",haltestellen," Haltestellen")

        print("Es steigen " ,einsteiger, "Personen ein") 


        if(int(Personen) > 60):
            print ("Es dürfen maximal 60 Personen einsteigen")
            Personen = 60

        elif (int(Personen) < 0):
            print("Es müssen mindestens 0 Personen im Bus sein")    



   





