from rest_framework import serializers

from .models import Customer, Location, Picture, Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField('get_coordinates')
    timezone = serializers.SerializerMethodField('get_timezone')

    class Meta:
        model = Location
        fields = [
            'region',
            'street',
            'city',
            'state',
            'postcode',
            'coordinates',
            'timezone'
        ]

    def get_coordinates(self, obj):
        return {
            'latititude': str(obj.latitude),
            'longitude': str(obj.longitude)
        }

    def get_timezone(self, obj):
        return {
            'offset': str(obj.timezone_offset),
            'description': str(obj.timezone_description)
        }


class LocationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = [
            'large',
            'medium',
            'thumbnail'
        ]


class CustomerSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    contacts = serializers.SerializerMethodField('get_contacts')
    pictures = PictureSerializer(source='picture')
    name = serializers.SerializerMethodField('get_name')

    class Meta:
        model = Customer
        fields = [
            'type',
            'gender',
            'name',
            'location',
            'email',
            'birthday',
            'registered',
            'contacts',
            'pictures',
            'nationality',
        ]

    def get_name(self, obj):
        return {
            'title': obj.title,
            'first': obj.first_name,
            'last': obj.last_name
        }

    def get_contacts(self, obj):
        types = {
            'mobile': 'mobileNumbers',
            'phone': 'telephoneNumbers'
        }
        contacts = {
            types['mobile']: [],
            types['phone']: []
        }

        for contact in obj.contacts.all():
            contact_type = types[contact.type]
            contacts[contact_type].append(contact.full_number)

        return contacts


class CustomerCreateSerializer(serializers.ModelSerializer):
    location = LocationCreateSerializer()
    picture = PictureSerializer()
    phone = serializers.CharField(
        max_length=14,
        required=False
    )
    cell = serializers.CharField(
        max_length=14,
        required=False
    )

    class Meta:
        model = Customer
        exclude = ('type', )

    def to_representation(self, value):
        return CustomerSerializer(value).data

    def create(self, validated_data):
        location = validated_data['location']
        picture = validated_data['picture']
        phone = validated_data.get('phone', None)
        cell = validated_data.get('cell', None)

        del validated_data['location']
        del validated_data['picture']
        if phone:
            del validated_data['phone']
        if cell:
            del validated_data['cell']

        location = Location.objects.create(**location)
        picture = Picture.objects.create(**picture)
        customer = Customer.objects.create(
            location=location,
            picture=picture,
            **validated_data
        )

        if phone:
            Contact.objects.create(
                customer=customer,
                number=phone,
                type='phone'
            ),
        if cell:
            Contact.objects.create(
                customer=customer,
                number=cell,
                type='mobile'
            )

        return customer
