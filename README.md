
Analyze Tweets using Kafka and Spark Streaming
-------------------------------------------------
1)Using twitter API, get the real time tweets from the twitter and ingest to Kafka.
2)Proccess the kafka data using spark streaming to track popular hashtags and trendsetters for each hashtag.



Requirement.
----------------
1)Install kafka with zookeeper cluster
2) Spark client or spark cluster




A) create twitter developer account
---------------------------------------
https://apps.twitter.com/


B) Install packages to execute twitter kafka procedure
------------------------------------------------------
pip install tweepy --index-url https://pypi.python.org/simple/
pip install kafka 
virtualenv --python=/usr/bin/python2.6 <path/to/new/virtualenv/>



C) Update twitter_config.py with twitter developer account secret key

D) Update kafka broker ip and topic name in kafka-twitter-producer.py 

E) Update zookeeper ip and topic name in spark-stream-tweets.py

E) Run kafka-twitter-producer.py  file



F)Run spark jobs
----------------------------------------------
spark-submit --jars /home/centos/spark-streaming-kafka-assembly_2.10-1.6.3.jar spark-stream-tweets.py 2 60
spark-submit --master yarn --jars /home/pnda/spark-streaming-kafka-assembly_2.10-1.6.3.jar spark-stream-tweets.py 2 60 





Get the tweets data like this example:
----------------------------------------------------------------------
https://jsoneditoronline.org/?id=b58b0d4e4cea4382b1f3b9ea0193a67a


1st Steps:
----------------------------------------------------------------------------------------
([u'@1997_0901com', u'@BTS_twt', u'kookxxsaao9o1'], [u'#\uc815\uad6d', u'#JK'])
([u'@taengame', u'llsukill'], [u'#LilTouch_Oh_GG'])
([u'@kimtaehyung_net', u'@BTS_twt', u'1230_1013_jimin'], [u'#\ubdd4', u'#\ud0dc\ud615'])
([u'@PrabhasSaahoFan', u'UdayCha61750718'], [u'#Prabhas'])
([u'@SimpleGain', u'@vuhtans', u'carlonge'], [u'#1DDRIVE', u'#VUHTANS'])
([u'@SUGACoffee309', u'@BTS_twt', u'lcsnte'], [u'#\ubc29\ud0c4\uc18c\ub144\ub2e8', u'#BTS', u'#\uc288\uac00', u'#SUGA', u'#\ubbfc\uc724\uae30', u'#\uc724\uae30'])
([u'@jypnation', u'vJOgj2bLcde1fjO'], [u'#JACKSON', u'#GOT7', u'#\uac13\uc138\ube10', u'#PresentYOU', u'#Lullaby'])
([u'@EMMMZbaeee', u'yaappong'], [u'#MULBERRYxSEOUL', u'#BLACKPINK'])
([u'@HealthRanger', u'studentveronica'], [u'#salad'])
([u'@5sosworldalerts', u'5soswith_fans'], [u'#5SOS', u'#TheGroup', u'#PCAs'])


2nd steps
-----------------------
('#BTSonAGT', (0, set([u'@AGT'])))
('#BTSonAGT', (0, set([u'@bts_bighit'])))
('#BTSonAGT', (1, set([u'SolRodr13968887'])))

('#BTSonAGT', (0, set([u'@spjm_vid'])))
('#BTSonAGT', (0, set([u'@BTS_twt'])))
('#BTSonAGT', (1, set([u'honesilk'])))


('#BTSonAGT', (0, set([u'@btsanalytics'])))
('#BTSonAGT', (0, set([u'@BTS_twt'])))
('#BTSonAGT', (1, set([u'_poemusician'])))

('#BTSonAGT', (0, set([u'@AGT'])))
('#BTSonAGT', (0, set([u'@bts_bighit'])))
('#BTSonAGT', (1, set([u'samiKONICARMY'])))



#3rd Step
------------------------------
('#BTSonAGT', (4, set([u'@btsanalytics', u'samiKONICARMY', u'@spjm_vid', u'@BTS_twt', u'@bts_bighit', u'honesilk', u'SolRodr13968887', u'_poemusician', u'@AGT'])))


