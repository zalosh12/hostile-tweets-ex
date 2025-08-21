from .fetcher import Fetcher
from .processor import Processor

class Manager:
    def __init__(self):
        self.fetcher = Fetcher()

