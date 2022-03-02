
def joido(szombat,vasarnap):
    if szombat > vasarnap:
        return('Szombaton volt jobb ido. Ennyi fok volt:',szombat)
    else:
        return('Vasárnap volt jobb ido.Ennyi fok volt:',vasarnap)


szombat = int(input('hany fok volt szombaton?'))
vasarnap = int(input('hany fok volt vasarnap?'))
print(joido(szombat,vasarnap))
#Józsi copyright
