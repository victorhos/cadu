import json
from http import HTTPStatus

import pytest
from model_mommy import mommy


@pytest.mark.django_db
class TestViews:

    def test_create_customer_with_success(
        self,
        client,
        customer_payload
    ):
        response = client.post(
            '/customer/',
            data=customer_payload,
            format='json'
        )

        assert response.status_code == HTTPStatus.CREATED

    def test_should_filter_customers_by_area_type(
        self,
        client,
        customer_payload
    ):
        mommy.make(
            'customers.Customer',
            location__state='alagoas',
            location__latitude='-46.361899',
            location__longitude='-2.196998',
            _quantity=5
        )
        mommy.make(
            'customers.Customer',
            location__state='alagoas',
            location__latitude='-54.777426',
            location__longitude='-26.155681',
            _quantity=2
        )

        response = client.get('/customers/?area_type=special')
        content = json.loads(response.content)

        assert content['count'] == 5
        assert response.status_code == HTTPStatus.OK

    def test_should_filter_customers_by_region(
        self,
        client,
        customer_payload
    ):
        mommy.make(
            'customers.Customer',
            location__state='alagoas',
            location__region='nordeste',
            _quantity=5
        )
        mommy.make(
            'customers.Customer',
            location__state='pernambuco',
            location__region='nordeste',
            _quantity=2
        )
        mommy.make(
            'customers.Customer',
            location__state='acre',
            location__region='norte',
            _quantity=1
        )

        response = client.get('/customers/?region=nordeste')
        content = json.loads(response.content)

        assert content['count'] == 7
        assert response.status_code == HTTPStatus.OK
