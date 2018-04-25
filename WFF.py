import requests
import sys


info = chr(27)+"[0;32m"+"""


 __          __  _       ______ _ _        ______                      
 \ \        / / | |     |  ____(_) |      |  ____|                     
  \ \  /\  / /__| |__   | |__   _| | ___  | |__ _   _ ___________ _ __ 
   \ \/  \/ / _ \ '_ \  |  __| | | |/ _ \ |  __| | | |_  /_  / _ \ '__|
    \  /\  /  __/ |_) | | |    | | |  __/ | |  | |_| |/ / / /  __/ |   
     \/  \/ \___|_.__/  |_|    |_|_|\___| |_|   \__,_/___/___\___|_|   
                                                                   

@Twitter:Angrymasther_
"""+chr(27)+"[0;37m" """

Sintaxis:  python Bypass_Fuzzer.py [archivo diccionario] [url]

Diccionario recomendados: https://thireus.frenchdev.com/SharedFiles/WordLists/WordLists-20111129.zip

Marcadores: [!] = Error , [$] = Esta direccion existe, pero necesita autorizacion
"""
try:

	diccionario = sys.argv[1] #Variable con el nombre del archivo.
	url = sys.argv[2] #Variable con la url
except IndexError:
	print chr(27)+"[0;41m"+"[!]Faltan opciones"
	print info
	sys.exit(1)


def probar(direccion): #Funcion que prueba las direcciones
	completada = url + "/" + direccion  #Creamos una direccion completa
	peticion = requests.get(completada) #Hacemos la peticion
	if peticion.status_code == 400:
		return 400
	if peticion.status_code == 403:
		return "[$] "+completada
	elif peticion.status_code != 404: #Comprovamos el status_code
		return completada #Devolvemos las que funcionan
	
try: #Abrimos el try por si el archivo no se encuentra
	o = open(diccionario,"r") #abrimos el archivo
	
except FileNotFoundError:
	print "[!] Archivo no encontrado"

lineas = o.readlines() #Lista con las lineas del diccionario

for linea in lineas:
	probado = probar(linea)
	if probado != None:
		print probado #probamos todas las lineas
	if probado == 400:
		print "La url a dado problemas, cumpruebala"
