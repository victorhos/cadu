from django.db import models


class Location(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=32)
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=4
    )
    longitude = models.DecimalField(
        max_digits=8,
        decimal_places=4
    )


class Timezone(models.Model):
    offset = models.CharField(max_length=16)
    description = models.CharField(max_length=255)


class Picture(models.Model):
    large = models.URLField()
    medium = models.URLField()
    thumbnail = models.URLField()


class Customer(models.Model):
    type = models.CharField(max_length=8)
    title = models.CharField(max_length=8)
    gender = models.CharField(max_length=16)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateTimeField()
    nationality = models.CharField(max_length=10)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    picture = models.ForeignKey(
        Picture,
        on_delete=models.CASCADE
    )


class Contact(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    type = models.CharField(max_length=16)
    number = models.CharField(max_length=16)
