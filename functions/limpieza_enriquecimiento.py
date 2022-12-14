'''Funciones juntar, limpiar, enriquecer y transformar nuestros
datos antes de cargarlos a una base de datos'''

#Importo las librerías necesarias para las funciones del archivo
import pandas as pd
import regex as re

# Escribo mis funciones
def resubs(regex, x):
    ''' 
    this function needs first to import regex as re. 
    It allows to substitute what it is found for an empty space.
    '''
    y=[]
    for i in x:
        y.append(re.sub(regex,'',i)) 
    return y
    

def refind(regex, x):
    ''' 
    this function needs first to import regex as re. 
    It it return what it is found under the regular expresion.
    '''
    y=[]
    for i in x:
        y.append(re.findall(regex,i))
    return y

        
