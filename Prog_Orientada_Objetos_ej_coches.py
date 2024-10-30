#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 20:03:06 2023

@author: laptop
"""


#############
# Ejercicio #
#___________#

# Crear la clase coche que incluya los atributos 
# "marca", "modelo", "longitud" y "precio"

class Coches:
    def __init__(self, marca, modelo, longuitud, precio):      #Los parametros declarados asi pueden ser alterados por el usuario
        self.marca = marca                 #Los parametros declarados asi, son fijos, en caso de q se les diera un valor especifico, inmutables para el usuario
        self.modelo = modelo
        self.longuitud = longuitud
        self.precio = precio
    
    def __del__(self):
        print(f" {self} se está borrando de la memoria")
    
    def __len__(self):                            
        return self.longuitud
    
    def __str__(self):
        return f"Coche marca {self.marca}, modelo {self.modelo} y precio {self.precio}"

    def __gt__(self, otro):
        return self.precio > otro.precio
    
    def __ne__(self, otro):
        return self.precio != otro.precio
    
    def rebaja(self, param):
        return self.precio - (param/100 * self.precio)

dir(Coches)

# Crear objetos de la clase coche
coche1 = Coches("Mercedes", "SUV", 440, 75000)
coche2 = Coches("Toyota", "Corolla", 465, 27000)
coche3 = Coches("Hyundai", "Tucson", 450, 28000)
coche4 = Coches("Lambo", "Diablo", 500, 100000)


# Atribuirles características que se creen al inicializar, basadas en datos
# introducidos al crear los objetos

# Atribuirles métodos que permitan imprimir en la pantalla:
# Un mensaje al borrar el objeto
#del(coche1)

# un valor de longitud
len(coche2)

# un valor al hacer print()
print(coche2)
print(coche3)

lista_coches = [coche4, coche2, coche3]
# Crear métodos que permitan comparar los coches por el precio:
# if coche1 > coche2:
#   pass
coche4 > coche2
coche3 != coche2
print(min(lista_coches))


"""
Crear un método que reduzca el precio del coche en un porcentaje 
introducido como argumento
"""
coche3.rebaja(25)

coche2.rebaja(5)
