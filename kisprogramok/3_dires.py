print("hires")

class Hiresnő:
    def __init__(self,név,foglalkozás,nemzetiség):
        self.név = név
        self.foglalkozás = foglalkozás
        self.nemzetiség = nemzetiség
    def előtag(self):
        if self.nemzetiség == 'a':
            return "Ms."
        else:
            return "Frau"

hires_nők = []
for _ in range(3):
    név = input('Add meg egy hires nő nevét')
    foglalkozás = input('add meg a foglalkozasod')
    nemzetiség = input('Add meg egy hires nő nemzetiségét (a/n)')
    hires_nő = Hiresnő(név, foglalkozás, nemzetiség)
    hires_nők.append(hires_nő)

for hires_nő in hires_nők:
    print(f'{hires_nő.előtag()} {hires_nő.név} egy híres,{hires_nő.foglalkozás}')