wr = open('bolt.txt','w')
ora = int(input(f'Hány ora van most'))
wr.write(f'{ora}\n')
if ora >= 8 and ora <= 16:
    print('nyitva van a bót')
    wr.write('nyitva van a bót')
else:
    print('nincs nyitva a bót')
    wr.write('nincs nyitva a bót')
wr.close()
