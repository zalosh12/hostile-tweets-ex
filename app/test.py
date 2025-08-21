from fetcher import Fetcher
import config
loader = Fetcher(
    uri=config.MDB_CONNECTION,
    db_name=config.DB_NAME,
    collection_name=config.COLLECTION_NAME
)

loader.connect()
df = loader.load_data()
print(df.head())
df.to_csv("tweets_data.csv",index=False)

# # או עם query מסוים
# df_filtered = loader.load_data({"age": {"$gt": 25}})
# print(df_filtered.head())



# from fetcher import Fetcher
# import config
#
# x = Fetcher(
#     connection_string=config.MDB_CONNECTION,
#     db_name=config.DB_NAME,
#     collection_name=config.COLLECTION_NAME
# )
#
# x.create_connection()
# x.get_all()
# res = x.convert_to_data_frame()
# print(res.head())
