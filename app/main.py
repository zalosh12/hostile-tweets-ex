from fastapi import FastAPI
from app.manager import Manager


manager = Manager()
app = FastAPI()

@app.get("/")
def get_data():
    processed_data = manager.get_process_data()
    return processed_data