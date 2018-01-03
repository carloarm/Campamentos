import pymongo

#Inicializamos la BD
from pymongo import MongoClient
client = MongoClient()
db = client.primer
# Creamos la conex
db = client.database
camps = db.camps
for camp in camps.find():
	print(camp)