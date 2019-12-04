import logging

import requests

logger = logging.getLogger(__name__)


class CustomerClient:

    def get_customers(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as error:
            logger.error(f'Error to get customers in {url}. Error: {error}')
            raise

        return response
