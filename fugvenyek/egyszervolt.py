wr = open("egyszervolt.txt","w")
szoveg = ("Egyszer volt, hol nem volt, htedhét országon is túl, volt egyszer egy szegény solyajozsef feladatmegoldasa. Annak volt egy fia meg egy kis tehénkéje.")
def hossz():
    return len(szoveg)
wr.write(f'{hossz()}')

def kapitalista():
    return szoveg.capitalize()
wr.write(f'{kapitalista()}')
def kozep():
    return szoveg.center(20)
wr.write(f'{kozep()}')    
def vegezdos():
    return szoveg.endswith(".")
wr.write(f'{vegezdos()}')
def megkereses():
    return szoveg.find("volt")
wr.write(f'{megkereses()}')
def szamos():
    return szoveg.isalnum()
wr.write(f'{szamos()}')
def alfas():
    return szoveg.isalpha()
wr.write(f'{alfas()}')
def kicsi():
    return szoveg.islower()
wr.write(f'{kicsi()}')
def joinolas():
    return "#".join(szoveg)
wr.write(f'{joinolas()}')
def kisi():
    return szoveg.lower()
wr.write(f'{kisi()}')
def speces():
    return szoveg.lstrip()
wr.write(f'{speces()}')
def levaltas():
    return szoveg.replace("Egyszer","Valamiko")
wr.write(f'{levaltas()}')
def rkeres():
    return szoveg.rfind("volt")
wr.write(f'{rkeres()}')
def rvalami():
    return szoveg.rstrip()
wr.write(f'{rvalami()}')
def szetvalasz():
    return szoveg.split()
wr.write(f'{szetvalasz()}')
def kezedes():
    return szoveg.startswith("Egyszer")
wr.write(f'{kezedes()}')
def xxx():
     return szoveg.strip()
wr.write(f'{xxx()}')
def keretescsere():
    return szoveg.swapcase()
wr.write(f'{keretescsere()}')
def cim():
    return szoveg.title()
wr.write(f'{cim()}')
def nagy():
    return szoveg.upper()
wr.write(f'{nagy()}')
wr.close()





































