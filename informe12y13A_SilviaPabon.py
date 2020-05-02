# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:59:47 2020

@author: --
"""
# ----- Paquetes y librerías ----- #

import random


# -----Funciones----- #

"""Punto 1"""
def imprimir(lista):
    print (lista)
    
"""Punto 3"""
def generador(listA, n):
    R = []
    t = random.sample(listA, n)
    R.append(t)
    return R

"""Punto 5"""
def combinador(listA, listB):
    R = []
    a = random.sample(listA, len(listA))
    b = random.sample(listB, len(listB))
    c = a+b
    d = random.sample(c, len(c))
    R.append(d)
    return R

# -----Principal----- #

cartas = ["Payne" , "Hendrix" , "Stone" , "Coffey" , "Whitaker" , "Pope" ,
          "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" ,
          "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" ,
          "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers" , 
          "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" ,
          "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" ,
          "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" ,
          "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" ,
          "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" ,
          "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher" , "Mcfadden" ,
          "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" ,
          "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat" , 
          "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns", 
          "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons", 
          "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" ,
          "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" ,
          "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" , "Mann"]

premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]


"""Punto 2"""
imprimir(cartas)
print("\n")
imprimir(premium)
print("\n")

"""Punto 4"""

jugador = generador(cartas, 10)

"""Punto 6"""
juego = combinador(cartas, premium)

# 7
sobre_uno = generador(juego, 5)

sobre_dos = generador(juego, 5)

sobre_tres = generador(juego, 5)
