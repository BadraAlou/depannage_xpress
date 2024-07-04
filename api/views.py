from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from depannagexpressapp.models import Commande
from api.serializers import *

#from .filters import ReservationFilter


class CommandeListCreate(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    filter_backends = [DjangoFilterBackend]
    #filterset_class = ReservationFilter
    filterset_fields = ('nom', 'depart', 'destination',)


class CommandeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer