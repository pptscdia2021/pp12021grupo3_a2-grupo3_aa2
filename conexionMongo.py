import pymongo
import pandas as pd
import csv

client = pymongo.MongoClient('localhost', 27017)
db = client['weatherHistory']
## Eliminar la colecction anterior para crear una nueva
db.weatherHistory.drop()
collection = db['weatherHistory']
df = pd.read_csv("/mongo/weatherHistory.csv")

## "records" significa que vamos a obtener el contenido separado por cada fila
data = df.to_dict(orient = "records") 
collection.insert_many(data)

print(client.list_database_names())
df.shape
df

collection.estimated_document_count()


