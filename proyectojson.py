#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

with open('monumentos-C_Leon.json') as data:
	doc = json.load(data)

print '1.- Listar los nombres de los monumentos'
print '2.- ¿Cuántos yacimientos arqueológicos hay?'
print '3.- Pide por teclado un nombre de monumento y muestra las coordenadas de ubicación'
print '4.- Pide por teclado una cadena y muestra las coincidencias encontradas en la descripción del monumento'
print '5.- Pide por teclado un precio minimo y maximo (también puede ser gratuito) y muestra aquellos monumentos con un precio entre dicho rango además de que el programa preguntará si quiere información acerca de un monumento en concreto.'


op = int(raw_input('\nElige una opción numérica de las indicadas: '))

#Enunciado 1
if op == 1:
	for x in doc['monumentos']:
		print x[u'nombre']
		
#Enunciado 2
if op == 2:
	for x in doc['monumentos']:
		if x[u'tipoMonumento'] == u'Yacimientos arqueológicos':
			print len(x)
			break
