from django.db import models
import time
# Create your models here.

class Region(models.Model):
    nom = models.CharField(max_length = 300)
    
    def __unicode__(self):
        return self.nom
    

class Magasin(models.Model):
    nom = models.CharField(max_length = 300)
    adress = models.TextField()
    tel = models.CharField(max_length = 50)
    fax = models.CharField(max_length = 50)
    region = models.ForeignKey(Region)
    
    def __unicode__(self):
       return self.nom

class Categorie(models.Model):
    nom = models.CharField(max_length = 300)
    
    def __unicode__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length = 300)
    prix_org = models.FloatField()
    prix_promo = models.FloatField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    folder_id = int(time.time())
    image = models.FileField(upload_to='uploads/%s/' % (folder_id) , blank = True)
    etat_choices = (
        ('Disponible', 'Disponible'),
        ('Limite','Limite'),
        ('ndispo', 'Disponible')
    )
    etat  = models.CharField(max_length = 50, choices = etat_choices)
    magasin = models.ForeignKey(Magasin)
    region = models.ForeignKey(Region)
    categorie = models.ForeignKey(Categorie)
    

