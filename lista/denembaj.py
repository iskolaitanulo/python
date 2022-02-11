fas = input('adja szoszt')
def nevelo(szo):
    maganhazok=['a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű']
    if szo[0] in maganhazok:
        return 'az'
    else:
        return 'a'
print(nevelo(fas),fas)
