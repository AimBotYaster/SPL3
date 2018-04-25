        #submission.py 

        # Level2 - korrekte Lösung ermittel
        # for  x in range (1,11,3) :

abgabe = "10:00:00 3 1 10:20:00 wrong 1 10:45:00 correct 2 10:20:01 correct:"
t = abgabe.split(" ")
startzeit = t[0]
#submissions = t [1]

print(abgabe)
submissions = t[1]
bestezeit = "23:59:59"
besteuser = -1

for position in range (2,len(t),3):
    user = t[position]
    zeit = t [position+1]
    loesung = t[position+2]
    print("Abgabe: ", user,zeit,loesung)
    if(zeit<bestezeit and loesung =="correct"):
            bestezeit = zeit
            besteruser = user




print(bestezeit, bestezeit)        
