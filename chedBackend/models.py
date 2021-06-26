from django.contrib.gis.db import models


class TiendasChedraui(models.Model):
    id_mg = models.BigIntegerField()
    nombre_che = models.CharField(max_length=254, null=True)
    formato = models.CharField(max_length=254, null=True)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    geom = models.MultiPointField(srid=4326)


# Auto-generated `LayerMapping` dictionary for TiendasChedraui model

