
def autotipi(autotipus):
    if autotipus[0] == "A" or autotipus[0] == "B":
        return("Nemet ato")
    else:
        return("nem nemet :C")
def gyartasiido(gyartasiev):
    if gyartasiev >= 2001 and gyartasiev != 2022:
        return("21.szazadi")
    elif gyartasiev == 2022:
        return("napjaink atoja")
    else:
        return("20. szazadi")

autotipus = input('Milyen auto tipusa')
gyartasiev = int(input('gyartasi eve'))
sebbesség = int(input('sebessege'))
print(autotipi(autotipus))
print(gyartasiido(gyartasiev))
