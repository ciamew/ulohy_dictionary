#zrataj pocet pismen v retazci
from string import ascii_lowercase
vstup = input("Zadaj mi retazec:")
pocitadlo = {} #alebo pocitadlo = dict()

for i in vstup:
    if i in ascii_lowercase:
        pocitadlo[i] = pocitadlo.get(i,0) + 1 #pocitadlo.get(i,0) ak tam pismeno je, vrati jeho hodnotu, ak nie je vrati 0 a zvacsi o 1
    # if i in pocitadlo.key(): #inak urobene
    #     pocitadlo[i] += 1
    # else:
    #     pocitadlo[i] = 1
print(pocitadlo)