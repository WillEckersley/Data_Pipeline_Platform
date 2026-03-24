import json
import time

from confluent_kafka import Producer
from data_source import Stream
from kafka_config import CONFIG, TOPIC
from logger import SendLogger
from random import randint
from logger_config import Log

if __name__ == "__main__":
    # Initialise the producer
    producer = Producer(CONFIG)

    # Create a data stream of fake messages
    stream = Stream()
    messages = stream.generate_message()

    for message in messages:
        json_message = json.dumps(message)
        try:
            producer.produce(
                topic=TOPIC,
                key=str(randint(1, 5)),
                value=json_message,
                callback=SendLogger.callback
            )
        except BufferError:
            Log.get_logger.warning("Queue full, waiting...")
            producer.poll(1)

        producer.poll(0)
        time.sleep(1)

    producer.flush()