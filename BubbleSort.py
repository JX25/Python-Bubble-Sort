import json
import sys


def bubbleSort(tablica):
    for i in range(0, len(tablica)-1, 1):
        for j in range(0, len(tablica)-i-1, 1):
            if tablica[j] > tablica[j+1]:
                tmp = tablica[j]
                tablica[j] = tablica[j+1]
                tablica[j+1] = tmp



with open(sys.argv[1]) as json_data:
    tab = json.load(json_data)
tab = tab["t"]
print "Sortowanie babelkowe"
print "Przed:"
print tab
print "Po:"
bubbleSort(tab)
print tab