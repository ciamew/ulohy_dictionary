pd = {} #prazdny dictionary
fz = {'a':0, 'b':5, 'jedlo':365, 7:23, 'jaj':[4,6,8]}

print(fz['b'])
print(fz['jaj'])
print(fz['jaj'][1]) #druhe [] printne cislo v zozname

for key in fz:
    print(key)
    print(fz[key])

print(fz)
print(*fz)