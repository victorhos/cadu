from rest_framework import serializers

from .models import Location, Timezone, Picture, Customer, Contact


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = ('id', )


class TimezoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timezone
        exclude = ('id', )


class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        exclude = ('id', )


class ContactSerializer(serializers.ModelSerializer):

    class Meta(serializers.ModelSerializer):
        model = Contact
        exclude = ('id', )


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        exclude = ('id', )
