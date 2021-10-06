név = input('Mi a gép neve?')
müködik = True if input("Müködik (i/n)") == 'i' else False
ár = int(input('Mi az ára?'))
if (név == 'ZX Spectrum' or név == 'C64') and müködik and ár <= 25000:
    print('az attila megoldása jobb xd')
else:
    print('szar az egész xd')