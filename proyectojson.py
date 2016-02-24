#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os


with open('monumentos.json') as data:
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
		print x["nombre"]
		
#Enunciado 2
if op == 2:
	suma = 0
	for x in doc["monumentos"]:
		if u"Yacimientos arqueológicos" in x["tipoMonumento"]:
			suma = suma + 1
	print suma
		
#Enunciado 3
if op == 3:
	nombre = raw_input("Di un nombre de algún monumento: ")
	for x in doc["monumentos"]:
		if nombre == x[u"nombre"]:
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
		if informacion in x[u'Descripcion']["__cdata"]:
			print x[u"Descripcion"][u"__cdata"]
			break

#Enunciado 5
if op == 5:
	gratis = raw_input("Es gratuito? ")
	if gratis.lower() == "si":
		for x in doc["monumentos"]:
			if "horariosYTarifas" in x:
				if "Gratuito" in x["horariosYTarifas"]["__cdata"]:
					print x["nombre"]
		pregunta = raw_input("Quieres obtener información de algún monumento? ")
		if pregunta.lower() == "si":
			pregunta2 = raw_input("¿De qué monumento quieres obtener información? ")
			#Traduzco a unicode para evitar problemas
			pregunta2 = unicode(pregunta2,encoding='utf-8')
			for x in doc["monumentos"]:
				if pregunta2 in x['nombre']:
					print x["horariosYTarifas"]["__cdata"]
					break
	if gratis.lower() == "no":
		minimo = raw_input("Di un precio minimo: ")
		maximo = raw_input("Di un precio máximo: ")
		for x in doc["monumentos"]:
			if "horariosYTarifas" in x:
				if "Gratuito" not in x["horariosYTarifas"]["__cdata"] and "Tarifa" in x["horariosYTarifas"]["__cdata"]:
					print x["nombre"]
					tarifas = x["horariosYTarifas"]["__cdata"].split("Tarifa</h3>")[1].split("&euro")[0]
					print tarifas
