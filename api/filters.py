# reservations/filters.py

import django_filters
from depannagexpressapp.models import Reservation

class ReservationFilter(django_filters.FilterSet):
    class Meta:
        model = Reservation
        fields = {
            'pack': ['exact'],
            'date': ['exact', 'gte', 'lte'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'phone_number': ['icontains'],
            'wedding_date': ['exact', 'gte', 'lte'],
            'address': ['icontains'],
        }
