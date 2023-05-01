#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:10:33 2019

@author: nooralindeflaten
"""

#%% oppgåve 1 a

tal1 = int(input('tal 1: '))
tal2 = int(input('tal 2: '))
tal3 = int(input('tal 3: '))

if tal1 < tal2 < tal3:
    print('desse tala er stigande')
elif tal1 > tal2 > tal3:
    print('desse tala er synkjande')
else:
    print('desse tala er verken stigande eller synkjande')



#%% oppgåve 2
#a

kort = input('kortbokstav engelsk: ')
if kort.lower() == 'd':
    print('ruter')
elif kort.lower() == 'h':
    print('hjerter')
elif kort.lower() == 's':
    print('spar')
elif kort.lower() == 'c':
    print('kløver')
    
#%% oppgåve 2b

kortstokk = {'A':'Ess', '2':'to', '3':'tre', '4':'fire', '5':'fem', '6':'seks',
             '7':'sju', '8':'åtte', '9':'ni', '10':'ti', 'J':'knekt', 'Q':'dame', 
             'K':'kong'}

kort = input('skriv inn kort: ').upper()
while kort not in kortstokk:
    print('ikke gyldig')
    kort = input('skriv inn kort: ').upper()

n = kortstokk[kort]
print(n)


#%% oppgåve 3a

valutta = {'EUR': 9.68551,
           'USD': 8.50373,
           'GBP': 11.0134,
           'SEK': 0.92950,
           'AUD': 6.06501,
           'NOK': 1.00000}

penge_sum = float(input('Pengesum: '))
valutta_input = input('kva valutta har du? : ').lower()

while valutta_input not in valutta:
    print('ikkje gyldig valutta')
    valutta_input = input('kva valutta har du?? :').lower()

kurs = valutta[valutta_input]
utrekning = penge_sum*kurs
print('om du har', penge_sum, valutta_input.upper(), 'har du %2.f' %utrekning, 'NOK')

#%% oppgåve 3b

valutta = {'EUR': 9.68551,
           'USD': 8.50373,
           'GBP': 11.0134,
           'SEK': 0.92950,
           'AUD': 6.06501,
           'NOK': 1.00000}

penge_sum = float(input("Pengesum i NOK: "))
valutta_input = input("Kva valutta vil du ha?: ").lower()

while valutta_input not in valutta:
    print('Ikkje gyldig valutta.')
    valutta_input2=input("Kva valutta har du?: ").lower()

kurs = valutta[valutta_input]
utrekning = penge_sum/kurs
print("Om du har", penge_sum, "NOK", "har du %.2f" %utrekning, valutta_input.upper())

#%% oppgåve 4

for i in range(10):
    potens = (i**3)
    print(i,"** 3 = ", potens)

#%% oppgåve 5 
    
start = int(input("Start tal: "))
stopp = int(input("Slutt tal: "))
n = int(input("Ditt deletal: "))
if start > stopp:
    print("Ugydlig!")
else:
    print("Verdiar mellom", start, "og", stopp, "som er delige på", n, ":")    
    for x in range(start, stopp+1):
        if x % n == 0:
            print(x)

#%% oppgåve 6a og b
            
def tilFahrenheit(celsius):
    return (celsius * 1.800) + 32

print("Celsius    Fahrenheit        Status")
status = ("Eg har det bra.")
for celsius in range(0,101,10):
    if celsius > 60:
        status = ("Eg sveittar i hel.")
        
    fahrenheit = tilFahrenheit(celsius)
    print("%7d %13d %25s" %(celsius, fahrenheit, status))
    
#%% oppgåve 7
    
def renteOkning(verdi, fra, til):
    terminer = int(til-fra)
    inflasjon_maal = 1.02
    verdi_fixed = (verdi*(inflasjon_maal)**(terminer))
    print("%.2f kr i år %d, med eit inflasjonsmål på %.2f årlig, er i %d verdt %.2f kr."
    % (verdi, fra, inflasjon_maal, til, verdi_fixed))
    
renteOkning(100, 1910, 2020)
    





























