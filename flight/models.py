from django.conf import settings
from django.db import models


class Crew(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)


class Flight(models.Model):
    route = models.ForeignKey(
        "Route",
        on_delete=models.CASCADE,
        related_name="route",
    )
    airplane = models.ForeignKey(
        "Airplane",
        on_delete=models.CASCADE,
        related_name="airplane",
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    crew = models.ManyToManyField(
        Crew,
        related_name="crew",
    )


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    flight = models.ForeignKey(
        Flight,
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        "Order",
        on_delete=models.CASCADE,
        related_name="order",
    )


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    ) # Write the code for auth user model


class Airplane(models.Model):
    name = models.CharField(max_length=120)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()
    airplane_type = models.ForeignKey(
        "AirplaneType",
        on_delete=models.CASCADE,
        related_name="airplane_type",
    )


class AirplaneType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,

    )


class Route(models.Model):
    source = models.ForeignKey(
        "Airport",
        on_delete=models.CASCADE,
        related_name="airport_source",
    )
    destination = models.ForeignKey(
        "Airport",
        on_delete=models.CASCADE,
        related_name="airport_destination",
    )
    distance = models.IntegerField()


class Airport(models.Model):
    name = models.CharField(max_length=120)
    closet_big_city = models.CharField(max_length=120)
