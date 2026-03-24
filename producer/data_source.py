import json
import time

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from faker import Faker 
from random import randint

class MessageCreator: 
    
    def __init__(self):
        self.fake = Faker("en_GB")

    def create_record(self):
        """ 
        Generates a single dummy record to send to a Kafka consumer
        """
        name = self.fake.name()
        address = self.fake.address()
        ts_raw = datetime.now()
        ts_str = ts_raw.isoformat()

        message = {
            "Id" : randint(0, 1000000),
            "Name" : name,
            "Address" : address,
            "Timestamp" : ts_str, 
            "ProductId" : randint(0, 1000000)
        }
        return message

class Stream:

    def __init__(self):
        self.creator = MessageCreator()

    def generate_message(self):
        """
        Creates a list of dummy data to sent to a kafka topic, simulating a data stream.
        """
        while True: 
            yield self.creator.create_record()