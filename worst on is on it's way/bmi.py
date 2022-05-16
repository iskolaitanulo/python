testomeg = float(input('adja meg a testömegét'))
magassag = float(input('adja meg a magassagat'))
def szamol():
    realmagas = magassag / 100
    bmi = testomeg / realmagas ** 2
    return bmi

def bmi():
    
    if bmi <= 16:
        return("ön súlyosan fogyatékos")
    elif bmi <= 18.5:
        return('alultáplált')
    elif bmi <= 25:
        return("ön egészesegfsdtd")
    elif bmi <= 30:
        return("dagat gefcv ")
    else:
        return('halal rad')
bmi()