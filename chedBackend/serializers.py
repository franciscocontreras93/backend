from rest_framework import serializers
from chedBackend.models import TiendasChedraui


class TiendasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ('id_mg',
                  'nombre',
                  'formato',
                  'longitud',
                  'latitud')
