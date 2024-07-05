from django.contrib import admin

from django.contrib import admin
from .models import Utilisateur, Commune, Quartier, Garage, EndUser, Gerant, Remorquage, Commande

admin.site.register(Utilisateur)
admin.site.register(Commune)
admin.site.register(Quartier)
admin.site.register(Garage)
admin.site.register(EndUser)
admin.site.register(Gerant)
admin.site.register(Remorquage)
admin.site.register(Commande)

