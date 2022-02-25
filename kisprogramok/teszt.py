wr = open('bolt.txt','w')
def hanyora(ora):
    if ora >= 8 and ora <= 16 :
        
        return ('nyitva volt a bot')
        
    else:
        
        return "nem volt nyitva a bot"

ora = int(input(f'Hány ora van most'))
print(hanyora(ora))
wr.write(f'{ora} ora van\n ')   
wr.write(f'{hanyora(ora)}') 
wr.close()
