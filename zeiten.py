# zeiten.py 
import sys

def zeitInSekunden(h,m,s):
    beginnzeit = 0 
    beginnzeit += h*3600
    beginnzeit+= m*60
    beginnzeit+= s
    return beginnzeit


p = sys.argv

beginnZeit = p[1]
endeZeit = p[2]
beginn = beginnZeit.split(":")

end = endeZeit.split(":")



h = int(beginn[0])
m = int(beginn[1])
s =int(beginn[2])

h1 = int(end[0])
m1 = int(end[1])
s1 =int(end[2])




a = zeitInSekunden (h,m,s)
e = zeitInSekunden (h1,m1,s1)
Differenz = e-a

print(Differenz)