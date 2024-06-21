from django.contrib import admin
from .models import Departement,Employe,Absence,Paiement
# Register your models here.
admin.site.register(Departement)
admin.site.register(Employe)
admin.site.register(Absence)
admin.site.register(Paiement)