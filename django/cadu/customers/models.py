from django.db import models

from .enums import ContactType
from .helpers import (get_ddi_by_nationality, get_region_by_state,
                      get_type_area, normalize_digits)


class Location(models.Model):
    region = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=32)
    timezone_offset = models.CharField(max_length=16)
    timezone_description = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=11,
        decimal_places=8
    )
    longitude = models.DecimalField(
        max_digits=11,
        decimal_places=8
    )

    def clean(self):
        self.region = get_region_by_state(self.state)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Picture(models.Model):
    large = models.URLField()
    medium = models.URLField()
    thumbnail = models.URLField()


class Customer(models.Model):

    GENDERS = (
        ('female', 'f'),
        ('male', 'm')
    )

    type = models.CharField(
        blank=True,
        null=True,
        max_length=32
    )
    title = models.CharField(max_length=8)
    gender = models.CharField(
        max_length=16,
        choices=GENDERS
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    registered = models.DateTimeField()
    nationality = models.CharField(
        max_length=2,
        default='BR'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    picture = models.ForeignKey(
        Picture,
        related_name='pictures',
        on_delete=models.CASCADE
    )

    def clean(self):
        self.type = get_type_area(
            latitude=self.location.latitude,
            longitude=self.location.longitude
        )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Contact(models.Model):
    customer = models.ForeignKey(
        Customer,
        related_name='contacts',
        on_delete=models.CASCADE
    )
    type = models.CharField(
        choices=ContactType.get_database_choices(),
        max_length=ContactType.get_database_max_length()
    )
    number = models.CharField(max_length=16)

    def clean(self):
        self.number = normalize_digits(self.number)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @property
    def get_ddi(self):
        return get_ddi_by_nationality(self.customer.nationality)

    @property
    def full_number(self):
        return f'+{self.get_ddi}{self.number}'
