from datetime import datetime

import pytest
from model_mommy import mommy
from rest_framework.test import APIClient


@pytest.fixture
def response_data():
    return {
        'results': [
            {
                'gender': 'female',
                'name': {
                    'title': 'mrs',
                    'first': 'alejandra',
                    'last': 'rodrigues'
                },
                'location': {
                    'street': '3833 rua santa catarina ',
                    'city': 'umuarama',
                    'state': 'santa catarina',
                    'postcode': 43646,
                    'coordinates': {
                        'latitude': '10.7186',
                        'longitude': '57.4596'
                    },
                    'timezone': {
                        'offset': '+3:00',
                        'description': 'Baghdad, Riyadh, Moscow, St. Petersburg'  # noqa
                    }
                },
                'email': 'alejandra.rodrigues@example.com',
                'dob': {
                    'date': '1974-05-16T14:46:15Z',
                    'age': 44
                },
                'registered': {
                    'date': '2013-03-06T16:09:16Z',
                    'age': 5
                },
                'phone': '(09) 7033-7406',
                'cell': '(54) 3190-3469',
                'picture': {
                    'large': 'https://randomuser.me/api/portraits/women/18.jpg',  # noqa
                    'medium': 'https://randomuser.me/api/portraits/med/women/18.jpg',  # noqa
                    'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/18.jpg'  # noqa
                }
            }
        ]
    }


@pytest.fixture
def customer():
    customer = mommy.make(
        'customers.Customer',
        title='mrs',
        first_name='alejandra',
        last_name='rodrigues',
        email='alejandra.rodrigues@example.com',
        birthday=datetime.now(),
        gender='female',
        registered=datetime.now(),
        nationality='BR',
        location__region='sul',
        location__street='3833 rua santa catarina ',
        location__city='umuarama',
        location__state='santa catarina',
        location__postcode=43646,
        location__latitude=10.7186,
        location__longitude=57.4596,
        location__timezone_offset='+3:00',
        location__timezone_description='Baghdad, Riyadh, Moscow, St. Petersburg',  # noqa
        picture__large='https://randomuser.me/api/portraits/women/18.jpg',
        picture__medium=(
            'https://randomuser.me/api/portraits/med/women/18.jpg'
        ),
        picture__thumbnail=(
            'https://randomuser.me/api/portraits/thumb/women/18.jpg'
        )
    )

    mommy.make(
        'customers.Contact',
        type='phone',
        number='0970337406',
        customer=customer
    )
    mommy.make(
        'customers.Contact',
        type='mobile',
        number='5431903469',
        customer=customer
    )

    return customer


@pytest.fixture
def customer_payload():
    return {
        'gender': 'female',
        'title': 'mrs',
        'first_name': 'ione',
        'last_name': 'da costa',
        'location': {
            'street': '8614 avenida viníedcius de morais',
            'city': 'ponta grossa',
            'state': 'rondônia',
            'postcode': '97701',
            'latitude': '-76.3253',
            'longitude': '137.9437',
            'timezone_offset': '-1:00',
            'timezone_description': 'Azores, Cape Verde Islands'
        },
        'email': 'ione.dacosta@example.com',
        'birthday': '1968-01-24T18:03:23Z',
        'registered': '2004-01-23T23:54:33Z',
        'phone': '(09) 7033-7406',
        'cell': '(54) 3190-3469',
        'picture': {
            'large': 'https://randomuser.me/api/portraits/women/46.jpg',
            'medium': 'https://randomuser.me/api/portraits/med/women/46.jpg',
            'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/46.jpg'  # noqa
        }
    }


@pytest.fixture
def client():
    client = APIClient()
    return client
