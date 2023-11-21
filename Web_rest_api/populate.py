import os
from datetime import datetime

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web_rest_api.settings")
django.setup()

from django.contrib.auth.hashers import make_password  # noqa: E402
from travelling_stones import models  # noqa: E402

personnes = [
    models.Personne(
        username="thibeau",
        hashtag="#THIBI",
        password=make_password("user123"),
    ),
    models.Personne(
        username="gert",
        hashtag="#GERT",
        password=make_password("user123"),
    ),
    models.Personne(
        username="gwen",
        hashtag="#GWEN",
        password=make_password("user123"),
    ),
    models.Personne(
        username="maintenance",
        hashtag="false",
        password=make_password("user123"),
    ),
]

for personne in personnes:
    personne.save()

pays = [
    models.Pays(nom="belgique"),
    models.Pays(nom="france"),
    models.Pays(nom="allemagne"),
    models.Pays(nom="luxembourg"),
]
for pay in pays:
    pay.save()

calloux = [
    models.Calloux(numero=1, photo="test.jpg", personne=personnes[0]),
    models.Calloux(numero=2, photo="test.jpg", personne=personnes[0]),
    models.Calloux(numero=3, photo="test.jpg", personne=personnes[0]),
]
for callou in calloux:
    callou.save()


adresses = [
    models.Adresse(
        ville="libramont",
        pays=pays[0],
        coord_gps_long=49.94458339537513,
        coord_gps_lat=5.106072914797573,
    ),
    models.Adresse(
        ville="libramont",
        lieu_dit="HERS",
        pays=pays[0],
        coord_gps_long=50.08977981922105,
        coord_gps_lat=5.466536633025826,
    ),
]
for adresse in adresses:
    adresse.save()

decouvertes = [
    models.Decouverte(
        datetime=datetime.now(),
        adresse=adresses[0],
        decouvreur=personnes[0],
        calloux=calloux[0],
    ),
    models.Decouverte(
        datetime=datetime.now(),
        adresse=adresses[0],
        decouvreur=personnes[0],
        calloux=calloux[1],
    ),
    models.Decouverte(
        datetime=datetime.now(),
        adresse=adresses[1],
        decouvreur=personnes[0],
        calloux=calloux[2],
    ),
]
for decouverte in decouvertes:
    decouverte.save()

photos = [
    models.Photo(path="test.jpg", decouverte=decouvertes[0]),
    models.Photo(path="test.jpg", decouverte=decouvertes[1]),
    models.Photo(path="test.jpg", decouverte=decouvertes[2]),
]
for photo in photos:
    photo.save()
