#!/usr/bin/env python
# -*- coding: utf-8 -*-

def labda_test():
    #mocniny = []
    #for i in range(1,21):
    #    mocniny.append(i**2)
    
    mocniny = {i: i**2 for i in range(1,21)}
    
    #print(mocniny)
    #print(mocniny.keys())
    #print(mocniny.values())
    #print(mocniny[10])
    #print(type(mocniny))
    
    for key, value in mocniny.items():
        print("{} - {}".format(key, value))
        
def soucin2(pole_cisel):
    vysledek = 1
    for cislo in pole_cisel:
        vysledek = vysledek * cislo
    return vysledek
    
def pis_uzivatele(username, aktivni=True):
    print("Username {} jeho aktivita je {}".format(username, aktivni))
    
def nacti_data():
    #f = open("mesice.txt", "r", encoding="UTF-8")
    #data = f.readlines()
    #data = [radka.rstrip('\n') for radka in data]
    with open("mesice.txt", "r", encoding="UTF-8") as f:
        data = data = f.read().splitlines()
    #data = f.read().splitlines()
    print (data)
#---------- MAIN: ----------
#labda_test()
#print(soucin2([5,6,54]))
#pis_uzivatele("franta", False)
#pis_uzivatele("Pepa")

nacti_data()