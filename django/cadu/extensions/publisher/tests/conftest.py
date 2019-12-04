import pytest
from model_mommy import mommy


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
        'customers.Curtomer',
        title='mrs',
        first_name='alejandra',
        last_name='rodrigues',
        email='alejandra.rodrigues@example.com',
        birthday='2013-03-06T16:09:16Z',
        gender='female',
        location__street='3833 rua santa catarina ',
        location__city='umuarama',
        location__state='santa catarina',
        location__postcode=43646,
        location__latitude=10.7186,
        location__longitude=57.4596,
        timezone__offset='+3:00',
        timezone__description='Baghdad, Riyadh, Moscow, St. Petersburg',
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
        number='(09) 7033-7406',
        customer=customer
    )
    mommy.make(
        'customers.Contact',
        type='phone',
        number='(54) 3190-3469',
        customer=customer
    )

    return customer
