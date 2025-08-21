from pymongo import MongoClient
import pandas as pd

class Fetcher:
    def __init__(self, uri: str, db_name: str, collection_name: str = "tweets"):
        self.uri = uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None

    def connect(self):
        self.client = MongoClient(self.uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

    def load_data(self) -> pd.DataFrame:
        if self.collection is None:
            raise Exception("Failed to load data")
        docs = list(self.collection.find({}))
        df = pd.DataFrame(docs)
        df = df.rename(columns={"_id":"id"})
        return df

    def close(self):
        if self.client:
            self.client.close()





