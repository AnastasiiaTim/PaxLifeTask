from django.db import models


class Airport(models.Model):
    ident = models.CharField(max_length=4, default='')
    type = models.CharField(max_length=15, default='')
    name = models.CharField(max_length=255, default='')
    latitude_deg = models.FloatField(default=0.00)
    longitude_deg = models.FloatField(default=0.00)
    elevation_ft = models.IntegerField(default=0)
    continent = models.CharField(max_length=2, default='')
    iso_country = models.CharField(max_length=2, default='')
    iso_region = models.CharField(max_length=5, default='')
    municipality = models.CharField(max_length=255, default='')
    scheduled_service = models.CharField(max_length=3, default='no')
    gps_code = models.CharField(max_length=4, default='')
    iata_code = models.CharField(max_length=3, default='')
    local_code = models.CharField(max_length=4, default='')
    home_link = models.CharField(max_length=255, default='')
    wikipedia_link = models.CharField(max_length=255, default='')
    keywords = models.CharField(max_length=4, default='')
