import os

# MDB_CONNECTION = os.getenv("MDB_CONNECTION", "mongodb://localhost:27017/")
MDB_USER = os.getenv("MDB_USER","IRGC")
MDB_PASSWORD = os.getenv("MDB_PASSWORD","iranianiranian")

MDB_CONNECTION = r"mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"
DB_NAME = os.getenv("DB_NAME","IranMalDB")
# MDB_CONNECTION = f"mongodb://{MDB_USER}:{MDB_PASSWORD}@mongodb-service:27017/"
# DB_NAME = os.getenv("DB_NAME", "enemy_soldiers")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "tweets")
