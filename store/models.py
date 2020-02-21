from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50, default='name')
    url = models.CharField(max_length=200)
    search_request = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % (self.url)

class Address(models.Model):
    address = models.CharField(max_length=200)
    shop_id = models.OneToOneField(Shop, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s %s" % (self.address, self.shop_id)

class Coordinates(models.Model):
    adress_id = models.OneToOneField(Address, on_delete=models.DO_NOTHING)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return "%s %s" % (self.lat, self.lon)