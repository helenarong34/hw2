import mediacloud.datetime
import configparser
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger= logging.getLogger(__name__)

#Source:
#http://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/

class MediaCloud:
    def get_api_key(self):
        logger.info('Getting API key from config file...')
        config = configparser.ConfigParser()

        try:
            config.read('../config.ini')
            self.api_key = config['MEDIACLOUD']['api_key']

        except Exception:
            logger.error('Failed to read file', exc_info=True)
    def make_mc_connection(self):
        self.mc_connection = mediacloud.api.media_cloud(self.apo_key)
        if self.mc_connection is None:
            logger.error('cannot make MediaCloud connection.')

    def handle_request(self,search_tuple,start_date,end_date):
        self.get_api_key()
        self.make_mc_connection
        logger.info('Handling request')
            logger.info('Search term(s): %s', search_tuple)
        logger.info('Start date: %s', start_date)
        logger.info('End date: %s', end_date)
        result = self.mc_connection.sentenceCount(str(search_tuple), solr_filter=[self.mc_connection.publish_date_query(datetime.date(start_date[0], start_date[1], start_date[2]), datetime.date(end_date[0], end_date[1], end_date[2])) ])
        logger.info('Return result: %s', result)
        return result

media_cloud=MediaCloud()
res1 =  media_cloud.handle_request(('Trump'), (2016, 9, 1), (2016, 9, 30))
res2 =  media_cloud.handle_request(('Clinton'), (2016, 9, 1), (2016, 9, 30))
print (res1['count'])
print (res2['count'])
