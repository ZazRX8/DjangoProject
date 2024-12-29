from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        upload_to='restaurant/static/restaurant/menu_items/menu_items', blank=True, null=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"