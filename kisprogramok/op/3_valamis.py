


def kiir(ora ,perc):
    return str(ora) + 'ora' + str(perc) + 'perc'
def oraperc(hossz):
    ora = hossz//60
    perc = hossz- ora * 60
    return kiir(ora, perc) 

for _ in range(3):
    cim = input('film neve')
    hossz = int(input('adja iőt faszfejT4EEAS '))
    print(f'film cime {cim} ennyi ideig  óráig tart {oraperc(hossz)} és ennyi pecig {hossz} ')
