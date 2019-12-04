import csv
import json
import logging
from io import StringIO

from cadu.customers.serializers import CustomerCreateSerializer

from .client import CustomerClient
from .helpers import build_payload_from_csv, build_payload_from_json

logger = logging.getLogger(__name__)


class PublisherCustomers:

    CSV_TYPE = 'text/csv'
    JSON_TYPE = 'application/json'

    def load_data(self, url):
        response = CustomerClient().get_customers(url)

        if response.headers['Content-type'] == self.CSV_TYPE:
            data = self._convert_csv_to_dict(response.content)
        if response.headers['Content-type'] == self.JSON_TYPE:
            data = self._build_json_data(response.content)

        self.save_customers(data)

    def save_customers(self, data):
        for item in data:
            customer_serializer = CustomerCreateSerializer(data=item)

            try:
                customer_serializer.is_valid(raise_exception=True)
                customer_serializer.save()
            except Exception as error:
                logger.warning(
                    f'Error to create customer with payload {item}. '
                    f'Error: {error}'
                )

    def _build_json_data(self, data):
        customers = []
        data = json.loads(data)

        for item in data['results']:
            customers.append(build_payload_from_json(item))

        return customers

    def _convert_csv_to_dict(self, data):
        customers = []

        data = data.decode('utf-8')
        csv_file = StringIO(data)
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)

        for row in reader:
            customers.append(build_payload_from_csv(row))

        return customers
