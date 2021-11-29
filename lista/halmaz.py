halmaz = {"nem","nemam"}
halmaz.clear
halmaz1 = {"tartalom","csaladbarat"}
halmaz2 = {"epikustartalom","csaladbarat"}
halmaz3=halmaz.copy()
kivonas = halmaz1.difference(halmaz2)
halmaz1.difference_update(halmaz2)
insert = halmaz1.intersection(halmaz2)
halmaz1.intersection_update(halmaz2)
isdisjoint = halmaz1.isdisjoint(halmaz2)

irok = {1,2,3}
rapeldat = {69,420,666,1,66,2,777,3}
irokraegypeldat = irok.issubset(rapeldat)
#hogyha az egyik halmaz tartalma tarltalmaza a másik tartalmat akkor truet ir ki másképp falset
irok = {1,2,3}
rapeldat = {69,420,666,1,66,2,777,3}
irokraegypeldat = irok.issuperset(rapeldat)
#


nincsbenne = {"ez","meg ez sincs","de ez igen*"}
bennevan = {"az","meg az sincs","de ez igen"}
benne = nincsbenne.symmetric_difference(bennevan)
#csak azt irja ki ami nincs benne mind2ben

halmazaz = {"getdicarded",88}
halmazaz.discard(88,69)
#removeoli az elemet amit megadunk és benne van de ami nincs benne azzal nem csinál semmit

unio = {"nincsötletem","ja"}
unio2 = {"minden tagot egy halmazba rak egyesiti az halmazokat"}
kozos = unio.union(unio2)

irok = {1,2,3}
rapeldat = {69,420,666,1,66,2,777,3}
irok.update(rapeldat)
#az update hozáadja az új elemeket az eredeti halmazhoz