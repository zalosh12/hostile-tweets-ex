import os

MDB_USER = os.getenv("MDB_USER","IRGC")

MDB_PASSWORD = os.getenv("MDB_PASSWORD","iranianiranian")

DB_NAME = os.getenv("DB_NAME","IranMalDB")

MDB_CONNECTION = r"mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"

# MDB_CONNECTION = rf"mongodb+srv://{MDB_USER}:{MDB_PASSWORD}@iranianmaldb.gurutam.mongodb.net/"

# DB_NAME = os.getenv("DB_NAME","IranMalDB")
# MDB_CONNECTION = f"mongodb://{MDB_USER}:{MDB_PASSWORD}@mongodb-service:27017/"
# COLLECTION_NAME = os.getenv("COLLECTION_NAME", "tweets")
