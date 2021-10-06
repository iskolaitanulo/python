nev = input(f"nevet adja meg")
bogyo = int(input("mennyi bogyo"))
if bogyo < 10:
    minosites = 'kicsike'
elif bogyo > 20:
    minosites = 'Hiper nagy csanád '
print( f'{nev} egy {minosites}')
