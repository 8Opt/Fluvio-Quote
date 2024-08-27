import time

from fluvio import Fluvio

from quote import generate_quote

TOPIC_NAME = "quote-daily"
PARTITION = 0

if __name__ == "__main__":
    # Connect to cluster
    fluvio = Fluvio.connect()

    producer = fluvio.topic_producer(TOPIC_NAME)

    while True: 
        quote = generate_quote()
        quote_str = quote.display()

        print(f"PUBLISHER: {quote_str}")
        producer.send_string("{}: timestamp: {}".format(quote_str, quote.created_at))
        time.sleep(7)

    # Flush the last entry
    producer.flush()
