def nev(n):
    if n != 0:
        nev(n-1)
        print('jozsiaisassa')
nev(100)