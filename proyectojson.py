#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pprint

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
	for x in doc["monumentos"]:
		print len(x["tipoMonumento"])
		
#Enunciado 3
if op == 3:
	nombre = raw_input("Di un nombre de algún monumento: ")
	for x in doc["monumentos"]:
		if nombre == x["nombre"]:
			latitud = x["coordenadas"]["latitud"]
			longitud = x["coordenadas"]["longitud"]
			print latitud, longitud
	pregunta = raw_input("¿Quieres verlo en el mapa? ")
	if pregunta == "si":
		print "http://www.openstreetmap.org/way/109089302#map=15/"+latitud+"/"+longitud

#Enunciado 4
if op == 4:
	informacion = raw_input("Di una cadena: ")
	for x in doc["monumentos"]:
		if informacion in x["Descripcion"]:
			print x["Descripcion"]
			break
