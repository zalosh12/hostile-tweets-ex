from app import config
from app.fetcher import Fetcher
from app.processor import Processor


class Manager:
    def __init__(self):
        self.fetcher = Fetcher(
            uri=config.MDB_CONNECTION,
            db_name=config.DB_NAME,
            # collection_name=config.COLLECTION_NAME
        )
        self.processor = Processor(r"C:\Users\eliwa\PycharmProjects\hostile-tweets-ex\data\weapon_list.txt")


    def process_data(self):
        self.fetcher.connect()
        df = self.fetcher.load_data()
        result_df = self.processor.process_data(df.copy())
        result_df = result_df.astype(str)
        filter_result_df = result_df[['id','original_text','rarest_word',"weapons_detected"]]
        output_data = filter_result_df.to_json(orient='records',force_ascii=False,indent=4)
        return output_data