from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
result = client['brazil']['cities'].find()

for i in result:
    print(i)
