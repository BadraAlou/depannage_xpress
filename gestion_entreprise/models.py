from django.db import models

class Departement(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def _str_(self):
     return self.nom
    

class Employe(models.Model):
    matricule = models.CharField(max_length=20, unique=True)
    nom = models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    date_embouche=models.DateField()
    

    def _str_(self):
        return f"{self.nom} {self.prenom}"
    
class Absence(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_absence = models.DateField()

    def _str_(self):
        return f"{self.employe.nom}-{self.date_absence}"
    

class Paiement(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement=models.DateField()

    def _str_(self):
        return f"{self.employe.nom}-{self.date_paiement}"