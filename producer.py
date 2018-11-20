#!/usr/bin/env python
"""
This script produce data from twitter to kafka
"""
# pylint: disable=invalid-name, import-error, bare-except, broad-except

import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream, API
from kafka import SimpleProducer, KafkaClient

from consoleLog import get_logger
from twitter_config import consumer_key, consumer_secret, access_token, access_token_secret

logger = get_logger("producer")

# Kafka settings
topic = "twitter-stream"
broker = "10.0.0.8:9092"
# setting up Kafka producer
try:
    kafka = KafkaClient(broker)
    producer = SimpleProducer(kafka)
except:
    message = "Unable to connect to the kafka " + sys.exc_info()
    logger.error(message)
    exit(0)



#This is a basic listener that just put received tweets to kafka cluster.
class StdOutListener(StreamListener):
    """stdout listener"""
    def on_connect(self):
        # Called initially to connect to the Streaming API
        logger.info("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        msg = "Error received: " + repr(status_code)
        logger.error(msg)
        return True  # Don't kill the stream

    def on_data(self, data):
        try:
            producer.send_messages(topic, data.encode('utf-8'))
            msg = "Twitter data: " + data
            logger.info(msg)
            logger.info("Succefully Twitter data send to kafka")
        except:
            msg = "Unable to send data to kafka"
            logger.error(msg)
            return False
        return True

    def on_timeout(self):
        return True # Don't kill the stream

WORDS_TO_TRACK = "the to and is in it you of for on my that at with me do have just this be so are not was but out up what now new from your like good no get all about we if time as day will one how can some an am by going they go or has know today there love more work too got he back think did when see really had great off would need here thanks been still people who night want why home should well much then right make last over way does getting watching its only her post his morning very she them could first than better after tonight our again down news man looking us tomorrow best into any hope week nice show yes where take check come fun say next watch never bad free life".split()

if __name__ == '__main__':
    logger.info("running the twitter-stream python code")
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener(api=API(wait_on_rate_limit=True,
                               wait_on_rate_limit_notify=True,
                               timeout=60, retry_delay=5,
                               retry_count=10,
                               retry_errors=set([401, 404, 500, 503])))
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    # Goal is to keep this process always going
    while True:
        try:
            # stream.sample()
            ret = stream.filter(languages=["en"], track=WORDS_TO_TRACK)
        except Exception as e:
            message = "Exception: " + e
            logger.error(message)
