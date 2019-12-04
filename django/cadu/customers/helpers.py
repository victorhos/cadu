import re

BOUNDING_BOX = {
    'special': [
        {
            'minlon': -2.196998,
            'minlat': -46.361899,
            'maxlon': -15.411580,
            'maxlat': -34.276938
        },
        {
            'minlon': -19.766959,
            'minlat': -52.997614,
            'maxlon': -23.966413,
            'maxlat': -44.428305
        }
    ],
    'normal': [
        {
            'minlon': -26.155681,
            'minlat': -54.777426,
            'maxlon': -34.016466,
            'maxlat': -46.603598
        }
    ]
}


def normalize_digits(string):
    return re.sub(pattern='[^\d+]', repl='', string=string)


def get_region_by_state(state):
    regions = {
        'amazonas': 'norte',
        'acre': 'norte',
        'rondônia': 'norte',
        'roraima': 'norte',
        'amapá': 'norte',
        'pará': 'norte',
        'tocantins': 'norte',
        'maranhão': 'nordeste',
        'piauí': 'nordeste',
        'rio grande do norte': 'nordeste',
        'ceará': 'nordeste',
        'paraíba': 'nordeste',
        'bahia': 'nordeste',
        'pernambuco': 'nordeste',
        'alagoas': 'nordeste',
        'sergipe': 'nordeste',
        'goiás': 'centro-oeste',
        'mato grosso': 'centro-oeste',
        'mato grosso do sul': 'centro-oeste',
        'distrito federal': 'centro-oeste',
        'minas gerais': 'sudeste',
        'espírito santo': 'sudeste',
        'rio de janeiro': 'sudeste',
        'são paulo': 'sudeste',
        'paraná': 'sul',
        'santa catarina': 'sul',
        'rio grande do sul': 'sul',
    }

    return regions[state]


def get_ddi_by_nationality(nationality):
    ddi = {
        'BR': 55
    }
    return ddi[nationality]


def get_type_area(latitude, longitude):
    BOUNDING_BOX = {
        'special': [
            {
                'minlon': -2.196998,
                'maxlon': -15.411580,
                'minlat': -46.361899,
                'maxlat': -34.276938
            },
            {
                'minlon': -19.766959,
                'maxlon': -23.966413,
                'minlat': -52.997614,
                'maxlat': -44.428305
            }
        ],
        'normal': [
            {
                'minlon': -26.155681,
                'maxlon': -34.016466,
                'minlat': -54.777426,
                'maxlat': -46.603598
            }
        ]
    }

    for area_type in BOUNDING_BOX.keys():
        for area in BOUNDING_BOX[area_type]:
            if (
                longitude >= area['maxlon'] and
                longitude <= area['minlon'] and
                latitude <= area['maxlat'] and
                latitude >= area['minlat']
            ):
                return area_type

    return 'laborious'
