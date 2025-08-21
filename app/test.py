from  manager import Manager

x = Manager()
y = x.get_process_data()
print(y)
# with open("nothing.json","w") as f:
#     f.write(y)

# from fetcher import Fetcher
# import config
# loader = Fetcher(
#     uri=config.MDB_CONNECTION,
#     db_name=config.DB_NAME,
#     # collection_name=config.COLLECTION_NAME
# )
#
# loader.connect()
# df = loader.load_data()
# print(df.head())
# # df.to_csv("tweets_data.csv",index=False)
# from processor import Processor
# a = Processor(r"C:\Users\eliwa\PycharmProjects\hostile-tweets-ex\data\weapon_list.txt")
# a.clean_text()
# p


