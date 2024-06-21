from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # URL pour la vue 'index'
    path('remorquage-simple.html', views.remorquage_simple, name='remorquage_simple'), # URL pour la vue 'privacy_policy'
    path('remorquage-reparation.html', views.remorquage_reparation, name='remorquage_reparation'), # URL pour la vue 'terms_conditions'
    path('repsur-place.html', views.repsur_place, name='repsur-place'),
    path('contact.html', views.contact, name='contact.html'),
    path('apropos.html', views.apropos, name='apropos.html'),
    path('index.html', views.index, name='index'), # URL pour la vue 'index'
    
]
