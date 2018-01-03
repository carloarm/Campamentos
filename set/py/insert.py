import pymongo
import json
import os, sys

#Leemos archivo JSON
if __name__ == '__main__':
	dir = os.path.dirname(sys.argv[0])
	print(dir)
	filename = dir + '\\res\\campamentos.json'
	print(filename)
	with open(filename) as data:
	    campsdata = json.load(data)

#Inicializamos la BD
from pymongo import MongoClient
client = MongoClient()
db = client.primer
# Creamos la conex
db = client.database
camps = db.camps
#Insertamos los campamentos en la BD
result = camps.insert_many(campsdata)
print("Resultados almacenados en la base de datos: " + result.inserted_ids)