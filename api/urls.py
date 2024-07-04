from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from api.views import *

urlpatterns = [
    path('', include(router.urls)),

    path('commandes/', CommandeListCreate.as_view(), name='commandes-list-create'),
    path('commandes/<int:pk>/', CommandeRetrieveUpdateDestroy.as_view(), name='commandes-detail'),
    
]