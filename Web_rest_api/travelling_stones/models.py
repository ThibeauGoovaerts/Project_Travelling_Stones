from django.contrib.auth.models import AbstractUser
from django.db import models


class Calloux(models.Model):
    numero = models.IntegerField()
    photo = models.FileField()
    personne = models.ForeignKey("Personne", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("personne", "numero")


class Pays(models.Model):
    nom = models.CharField(max_length=100, default="Belgique", primary_key=True)


class Adresse(models.Model):
    ville = models.CharField(max_length=100)
    lieu_dit = models.CharField(blank=True, max_length=100)
    coord_gps_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    coord_gps_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    pays = models.ForeignKey("Pays", on_delete=models.DO_NOTHING, default="Belgique")


class Personne(AbstractUser):
    username = models.CharField(max_length=100, primary_key=True)
    hashtag = models.CharField(max_length=100)
    REQUIRED_FIELDS = ["hashtag"]


class Decouverte(models.Model):
    datetime = models.DateTimeField(auto_now=True)
    decouvreur = models.ForeignKey("Personne", on_delete=models.CASCADE)
    adresse = models.ForeignKey("Adresse", on_delete=models.CASCADE)
    calloux = models.ForeignKey("Calloux", on_delete=models.CASCADE)


class Photo(models.Model):
    path = models.FileField()
    decouverte = models.ForeignKey("Decouverte", on_delete=models.CASCADE, blank=False)
