import pytest

from cadu.customers.models import Customer
from cadu.extensions.publisher.publisher import PublisherCustomers


@pytest.mark.django_db
class TestPublisher:

    def test_load_data_from_csv_with_success(self):
        cc = PublisherCustomers()
        cc.load_data(
            url='https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv'  # noqa
        )

        assert Customer.objects.count() == 1000

    def test_load_data_from_json_with_success(self):
        cc = PublisherCustomers()
        cc.load_data(
            url='https://storage.googleapis.com/juntossomosmais-code-challenge/input-frontend-apps.json'  # noqa
        )

        assert Customer.objects.count() == 200
