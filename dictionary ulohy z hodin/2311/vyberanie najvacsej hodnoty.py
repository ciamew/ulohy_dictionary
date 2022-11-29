#z daneho zoznamu vypise 3 polozky s najvacsou hodnotou

slov = {'a':0, 'b':5, 'jedlo':365, 'hhh':23, 'coje':875}

#1. podla funkcie sorted #sorted(slov,x) #x je druhy parameter aby triedilo podla hodnot

#2. podla bubblesort

#3. podla maximalneho prvku v slovniku

for y in range(3):
    max = slov['a']
    indexmax = 'a'
    for i in slov:
        if slov[i]:
            max = slov[i]
            indexmax = i
    print(max, indexmax)
    vymazat = slov.pop(indexmax)