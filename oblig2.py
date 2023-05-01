#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:08:17 2019

@author: nooralindeflaten
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random
def oppgave1():
 """ Printer ut store tall i kort og lang form,
 ofte kalt amerikansk og britisk form.
 """
 store_tall = [
 ["Million", "10^6 ", "10^6 "],
 ["Milliard", " ", "10^9 "],
 ["Billion", "10^9 ", "10^12"],
 ["Billiard", " ", "10^15"],
 ["Trillion", "10^12", "10^18"],
 ["Quadrillion","10^15", "10^24"],
 ["Quintillion","10^18", "10^30"],
 ["Sextillion", "10^21", "10^36"]
 ] # Hentet fra https://en.wikipedia.org/wiki/Names_of_large_numbers
 
  print("navn         lang    kort")
    for tall in store_tall:
        print(tall[0], tall[1], tall[2])
 pass
# I billion USD (kort form)
microsoft_inntekt_dollar = [
    [2002, 28.37],
    [2003, 32.19],
    [2004, 36.84],
    [2005, 39.79],
    [2006, 44.28],
    [2007, 51.12],
    [2008, 60.42],
    [2009, 58.44],
    [2010, 62.48],
    [2011, 69.94],
    [2012, 73.12],
    [2013, 77.85],
    [2014, 86.83],
    [2015, 93.58],
    [2016, 85.32],
    [2017, 89.95],
    [2018, 110.36],
    [2019, 125.84]
]  # Hentet fra https://www.statista.com/statistics/267805/microsofts-global-revenue-since-2002/

def oppgave2():
 
    Verdier_liste = []
    Ferdig = False

    while not Ferdig:
        Verdier = (input('Enter Value: '))
        if Verdier == 'Ferdig':
            Ferdig = True
            break
        else: 
            Verdier_liste.append(int(Verdier))
        
        Verdier_liste.sort()

    if len(Verdier_liste)%2 == 0:
        Lengde = len(Verdier_liste)
        Tall1 = Verdier_liste[Lengde//2]
        Tall2 = Verdier_liste[(Lengde//2)-1]
        Summen = (Tall1 + Tall2)/2
        print('The Median of the values are: ', Summen)
    
    else:
        Lengde = len(Verdier_liste)
        Median = (Lengde-1)//2
        print('The Median of the values are: ', Verdier_liste[Median])
        
def oppgave3a():
 """ Konverterer inntektene fra dollar til kroner
 uten Ã¥ gjÃ¸re endringer pÃ¥ originallisten.
 """
microsoft_inntekt_dollar = [
 [2002, 28.37],
 [2003, 32.19],
 [2004, 36.84],
 [2005, 39.79],
 [2006, 44.28],
 [2007, 51.12],
 [2008, 60.42],
 [2009, 58.44],
 [2010, 62.48],
 [2011, 69.94],
 [2012, 73.12],
 [2013, 77.85],
 [2014, 86.83],
 [2015, 93.58],
 [2016, 85.32],
 [2017, 89.95],
 [2018, 110.36],
 [2019, 125.84]
 ]

mikrosoft_inntekt_NOK = mikrosoft_inntekt_dollar.list * 8.6862 

print(mikrosoft_inntekt_NOK)

 pass
def oppgave3b():
 """ Tegner et histogram over inntektene til Microsoft
 """
 pass
def oppgave3c():
 """ Summerer opp inntektene til Microsoft
 """
 pass
def print_kart(kart):
 ''' Printer et 10 * 10 kart per rad
 input:
 kart, en list
 return:
 None'''
 for rad in kart:
 print("".join(rad))
def oppdater_kart(spillerX, spillerY, monsterX, monsterY):
 ''' Printer et 10 * 10 kart med spiller i posisjon (spillerX, spillerY)
 og monster i posisjon (monsterX, monsterY)
 input:
 spillerX og spillerY, heltall mellom 0 og 9
 return:
 None
 '''
 kart = []

 # Lag kart her ->
 print_kart(kart)


def flytt_spiller(bevegelse, spillerX, spillerY):
 ''' Flytt spiller hvis lovlig trekk
 input:
 bevegelse: w,a,s,d
 spillerX og spillerY, heltall mellom 0 og 9
 return:
 spillerX, spillerY, heltall mellom 0 og 9
 '''
 pass

def oppgave4():
 ''' Spill mot monster'''
 pass
def main():
 """ Dette er filens main-funksjon, det er denne funksjonen som kjÃ¸rer
 nÃ¥r hele filen blir kjÃ¸rt.
 Hvis du vil kjÃ¸re en av oppgave-funksjonene nedenfor fjerner du #-tegnet
 foran oppgave-funksjonen slik at den blir "skrudd pÃ¥".
 FÃ¸r du leverer kan det vÃ¦re lurt Ã¥ sjekke alle funksjonene. Dette gjÃ¸r
 du ved Ã¥ fjerne alle #-tegnene nedenfor.
 """
 # oppgave1()
 # print()
 # oppgave2a()
 # print()
 # print()
 # oppgave3a()
 # print()
 # oppgave3b()
 # print()
 # oppgave3c()
 # print()
 #oppgave4()
 #print()
main()