import sys
oldout = sys.stdout
print("Kepernyore ir.")
wr = open("test2.txt","w")
sys.stdout = wr
print("fajba iras")
wr.close()
print ( " Hova ir? " ) 
sys.stdout = oldout