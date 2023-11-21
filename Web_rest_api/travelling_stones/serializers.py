from rest_framework import serializers

from .models import Adresse
from .models import Calloux
from .models import Decouverte
from .models import Pays
from .models import Personne
from .models import Photo


class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = ["username", "password", "hashtag"]


class CallouxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calloux
        fields = ["numero", "photo", "personne"]


class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = "__all__"


class AdresseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresse
        fields = "__all__"


class DecouverteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decouverte
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"
