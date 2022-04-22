from modulsa import *
wr = open('jegyzet.txt','w')
stop = input("fajl nevet adja meg")
while stop != "stop":
    stop = input("akarsz még irni?")
    ff = input("adja meg mit akar irni")
    f = ff
    wr.write(f)
wr.close()