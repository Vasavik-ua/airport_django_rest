from django.conf import settings
from django.db import models


class Crew(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)


class Flight(models.Model):
    route = models.CharField(max_length=120)
    airplane = models.CharField(max_length=120)
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
    )


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders"
    ) # Write the code for auth user model
