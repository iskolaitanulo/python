def betukkel(szam):
    szamoknev = ['nulla','egy','kettő','három','négy','öt']
    return szamoknev[szam]

for szam in range(6):
    print(szam,betukkel(szam))