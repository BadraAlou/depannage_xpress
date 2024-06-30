from django.db import models

from django.db import models

# Utilisateurs
class Utilisateur(models.Model):
    user_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

# Communes
class Commune(models.Model):
    commune_id = models.AutoField(primary_key=True)
    nom_commune = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_commune

# Quartiers
class Quartier(models.Model):
    quartier_id = models.AutoField(primary_key=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    nom_quartier = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_quartier

# Garages
class Garage(models.Model):
    garage_id = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    quartier = models.ForeignKey(Quartier, on_delete=models.CASCADE)
    nom_garage = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.nom_garage

# EndUsers
class EndUser(models.Model):
    enduser_id = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nom} {self.prenom}'

# Gérants
class Gerant(models.Model):
    gerant_id = models.AutoField(primary_key=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)
    nom_gerant = models.CharField(max_length=255)
    prenom_gerant = models.CharField(max_length=255)
    type_gerant = models.CharField(max_length=255)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nom_gerant} {self.prenom_gerant}'


# Remorquages
class Remorquage(models.Model):
    remorquage_id = models.AutoField(primary_key=True)
    enduser = models.ForeignKey(EndUser, on_delete=models.CASCADE)
    gerant = models.ForeignKey(Gerant, on_delete=models.CASCADE)
    localisation = models.CharField(max_length=255)
    demande_date = models.DateField()
    re_description = models.CharField(max_length=255)
    besoin_auto = models.CharField(max_length=255)

    def __str__(self):
        return f'Remorquage {self.remorquage_id}'
    
    

