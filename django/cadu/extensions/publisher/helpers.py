def build_payload_from_csv(data):
    return {
        'gender': data[0],
        'title': data[1],
        'first_name': data[2],
        'last_name': data[3],
        'location': {
            'street': data[4],
            'city': data[5],
            'state': data[6],
            'postcode': data[7],
            'latitude': data[8],
            'longitude': data[9],
            'timezone_offset': data[10],
            'timezone_description': data[11],
        },
        'email': data[12],
        'birthday': data[13],
        'registered': data[15],
        'cell': data[17],
        'phone': data[18],
        'picture': {
            'large': data[19],
            'medium': data[20],
            'thumbnail': data[21]
        }
    }


def build_payload_from_json(data):
    return {
        'gender': data['gender'],
        'title': data['name']['title'],
        'first_name': data['name']['first'],
        'last_name': data['name']['last'],
        'location': {
            'street': data['location']['street'],
            'city': data['location']['city'],
            'state': data['location']['state'],
            'postcode': data['location']['postcode'],
            'latitude': data['location']['coordinates']['latitude'],
            'longitude': data['location']['coordinates']['longitude'],
            'timezone_offset': data['location']['timezone']['offset'],
            'timezone_description': data['location']['timezone']['description'],  # noqa
        },
        'email': data['email'],
        'birthday': data['dob']['date'],
        'registered': data['registered']['date'],
        'phone': data['phone'],
        'cell': data['cell'],
        'picture': {
            'large': data['picture']['large'],
            'medium': data['picture']['medium'],
            'thumbnail': data['picture']['thumbnail']
        }
    }
