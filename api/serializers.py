from depannagexpressapp.models import *
from rest_framework import serializers

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

# class ReservationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Commande
#         fields = '__all__'

