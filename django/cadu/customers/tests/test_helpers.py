import pytest

from cadu.customers.helpers import (get_ddi_by_nationality,
                                    get_region_by_state, get_type_area,
                                    normalize_digits)


class TestHelpers:

    @pytest.mark.parametrize('string,expected', [
        ('as1duif2j3LOç;4,.5', '12345'),
        ('ad   1 fd 2    3 4fdafda^~~5', '12345'),
        ('12345', '12345'),
        ('           12345   ', '12345')
    ])
    def test_should_normalize_digits(self, string, expected):
        assert normalize_digits(string) == expected

    def test_get_region_by_state_should_return_region(self):
        assert get_region_by_state('amazonas') == 'norte'

    def test_get_ddi_by_nationality_should_return_number(self):
        assert get_ddi_by_nationality('BR') == 55

    @pytest.mark.parametrize(
        'latitude,longitude,region_type_expected',
        [
            (-46.361899,  -2.196998, 'special'),
            (-44.428305, -23.966413, 'special'),
            (-54.777426, -26.155681, 'normal'),
            (1, 10, 'laborious')
        ]
    )
    def test_get_region_by_state_should_return_type_with_succes(
        self,
        latitude,
        longitude,
        region_type_expected
    ):
        region_type = get_type_area(latitude, longitude)

        assert region_type == region_type_expected
