kedd = int(input('Mennyit költötté kedden'))
szerda = int(input('Mennyit költötté szerda'))

if kedd > szerda:
    print('kedden költött többet ennyivel:',kedd - szerda,'fttal')
elif szerda == kedd:
    print('egyenlo')
else:
    print('szerdán költött többet',szerda - kedd,'fttal')
# Józsi copyright all rights reserved 