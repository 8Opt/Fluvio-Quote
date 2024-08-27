
from fluvio import Fluvio, Offset

TOPIC_NAME = "quote-daily"
PARTITION = 0

if __name__ == "__main__":
   # Connect to cluster
    fluvio = Fluvio.connect()
    consumer = fluvio.partition_consumer(TOPIC_NAME, PARTITION)

    while True: 
        # Consume last 1 records from topic
        for record in consumer.stream(Offset.from_end(0)):
            print(f"CONSUMER: {record.value_string()}")