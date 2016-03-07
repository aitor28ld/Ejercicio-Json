#!/usr/bin/env python
# coding: utf-8 
import json

import os

with open('monumentosjson.json') as data:
	doc = json.load(data)

print '1.- Listar los nombres de los monumentos'
print '2.- ¿Cuántos yacimientos arqueológicos hay?'
print '3.- Pide por teclado un nombre de monumento y muestra las coordenadas de ubicación'
print '4.- Pide por teclado una cadena y muestra las coincidencias encontradas en la descripción del monumento'
print '5.- Pregunta por teclado si el monumento a buscar es gratuito o no. Si la respuesta es sí, muestra el nombre de los monumentos gratuitos además de preguntar si desea obtener información de ellos. Si la respuesta es no, pedirá un precio máximo y mínimo mostrando los monumentos con la entrada en dicho rango y también preguntará si desea conocer información de alguno.'
print '6.- Genera un fichero HTML con el nombre, descripción y url del mapa de todos los monumentos'

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
	else:
		print "Gracias por utilizar nuestro servicio"

#Enunciado 4
if op == 4:
	informacion = raw_input("Di una cadena: ")
	for x in doc["monumentos"]:
		if informacion in x[u'Descripcion']["__cdata"]:
			print x[u"Descripcion"][u"__cdata"]
			break
			
#Enunciado 5
if op == 5:
	gratis = raw_input("¿El monumento a consultar es gratuito? ")
	if gratis.lower() == "si":
		for x in doc["monumentos"]:
			if "horariosYTarifas" in x:
				if "Gratuito" in x["horariosYTarifas"]["__cdata"]:
					print x["nombre"]
		pregunta = raw_input("\n¿Quieres obtener información de algún monumento? ")
		if pregunta.lower() == "si":
			pregunta2 = raw_input("\n¿De qué monumento quieres obtener información? ")
			#Traduzco a unicode para evitar problemas
			for x in doc["monumentos"]:
				if pregunta2 == x["nombre"].encode("utf-8") or pregunta2 in x["nombre"].encode("utf-8"):
					print x["horariosYTarifas"]["__cdata"]
					break
		else:
			print "Gracias por usar nuestro servicio"
	if gratis.lower() == "no":
		minimo = float(raw_input("Di un precio minimo: "))
		maximo = float(raw_input("Di un precio máximo: "))
		for x in doc["monumentos"]:
			if "horariosYTarifas" in x:
				if "Gratuito" not in x["horariosYTarifas"]["__cdata"] and "Tarifa" in x["horariosYTarifas"]["__cdata"] and "Este portal" not in x["horariosYTarifas"]["__cdata"] and "Contactar" not in x["horariosYTarifas"]["__cdata"]:
					tarifa = x["horariosYTarifas"]["__cdata"].split("Tarifa</h3>")[1].split("&euro")[0]
					if "General" in tarifa:
						tarifa2 = float(tarifa.split(":")[1])
						if minimo < tarifa2 and maximo > tarifa2:
							print "La entrada al monumento",x["nombre"],"cuesta",tarifa2, "euros"
					else:
						tarifa3 = float(tarifa)
						if minimo < tarifa3 and maximo > tarifa3:
							print "la entrada al monumento",x["nombre"],"cuesta", tarifa3,"euros"
					
		pregunta = raw_input("\n¿Quieres obtener información de algún monumento? ")
		if pregunta.lower() == "si":
			pregunta2 = raw_input("\n¿De qué monumento quieres obtener información? ")
			#Traduzco a unicode para evitar problemas
			for x in doc["monumentos"]:
				if pregunta2 == x["nombre"].encode("utf-8") or pregunta2 in x["nombre"].encode("utf-8"):
					print x["horariosYTarifas"]["__cdata"]
					break
		else:
			print "\nGracias por usar nuestro servicio"	
if op == 6:		
	for x in doc[u"monumentos"]:
		if "Descripcion" not in x:
			print "No existe Descripcion"
		else:
			os.system("echo '<h1>"+x[u"nombre"].encode("utf-8")+"</h1>' >> monumentos.html")
			os.system("echo '<p>"+x["Descripcion"]["__cdata"].encode("utf-8")+"</p>' >> monumentos.html")
			os.system("echo '<a href ='http://www.openstreetmap.org/way/109089302#map=15/"+x["coordenadas"]["latitud"]+"/"+x["coordenadas"]["longitud"]+"'>Mapa</a>' >> monumentos.html")
else:
	print "Opción inválida"			
