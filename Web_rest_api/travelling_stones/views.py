from django.contrib.auth.hashers import make_password
from django.http import Http404
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Adresse
from .models import Calloux
from .models import Decouverte
from .models import Pays
from .models import Personne
from .models import Photo
from .permissions import IsOwner
from .permissions import IsUser
from .serializers import AdresseSerializer
from .serializers import CallouxSerializer
from .serializers import DecouverteSerializer
from .serializers import PaysSerializer
from .serializers import PersonneSerializer
from .serializers import PhotoSerializer


class PersonneList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Personne.objects.all()

    def get(self, request, format=None):
        personnes = Personne.objects.all()
        serializer = PersonneSerializer(personnes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data["password"] = make_password(request.data["password"])
        serializer = PersonneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonneDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser | IsUser
    ]
    queryset = Personne.objects.all()

    def get_object(self, pk):
        try:
            return Personne.objects.get(pk=pk)
        except Personne.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        personne = self.get_object(pk)
        serializer = PersonneSerializer(personne)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        personne = self.get_object(pk)
        personne.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CallouxList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Calloux.objects.all()

    def get(self, request, format=None):
        calloux = Calloux.objects.all()
        serializer = CallouxSerializer(calloux, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = Personne.objects.get(username=request.user)
        request.data["personne"] = user.username
        serializer = CallouxSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CallouxListByUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Calloux.objects.all()

    def get(self, request, personne, format=None):
        user = Personne.objects.get(username=personne)
        calloux = Calloux.objects.all().filter(personne=user)
        serializer = CallouxSerializer(calloux, many=True)
        return Response(serializer.data)


class CallouxById(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Calloux.objects.all()

    def get(self, request, id, format=None):
        calloux = Calloux.objects.get(id=id)
        serializer = CallouxSerializer(calloux)
        return Response(serializer.data)


class CallouxDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser | IsOwner
    ]
    queryset = Calloux.objects.all()

    def get_object(self, personne, numero):
        try:
            return Calloux.objects.get(personne=personne, numero=numero)
        except Calloux.DoesNotExist:
            raise Http404

    def get(self, request, format=None, **kwargs):
        calloux = self.get_object(
            personne=kwargs.get("personne"), numero=kwargs.get("numero")
        )
        serializer = CallouxSerializer(calloux)
        return Response(serializer.data)

    def delete(self, request, format=None, **kwargs):
        calloux = self.get_object(
            personne=kwargs.get("personne"), numero=kwargs.get("numero")
        )
        calloux.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DecouverteList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Decouverte.objects.all()

    def get(self, request, format=None):
        decouvertes = Decouverte.objects.all()
        serializer = DecouverteSerializer(decouvertes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if "calloux" in request.data:
            calloux_args = request.data["calloux"]
            calloux = Calloux.objects.get(
                personne=Personne.objects.get(hashtag=calloux_args["hashtag"]),
                numero=calloux_args["numero"],
            )
            request.data["calloux"] = calloux.pk
        serializer = DecouverteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DecouverteListByCalloux(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Decouverte.objects.all()

    def get(self, request, format=None, **kwargs):
        decouvertes = Decouverte.objects.all()
        calloux = Calloux.objects.get(
            personne=Personne.objects.get(username=kwargs.get("personne")),
            numero=kwargs.get("numero"),
        )
        decouvertes = Decouverte.objects.all().filter(calloux=calloux)
        serializer = DecouverteSerializer(decouvertes, many=True)
        return Response(serializer.data)


class DecouverteListByUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Decouverte.objects.all()

    def get(self, request, personne, format=None):
        p = Personne.objects.get(username=personne)
        decouvertes = Decouverte.objects.all().filter(decouvreur=p)
        serializer = DecouverteSerializer(decouvertes, many=True)
        return Response(serializer.data)


class DecouverteDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser | IsOwner
    ]
    queryset = Decouverte.objects.all()

    def get_object(self, pk):
        try:
            return Decouverte.objects.get(pk=pk)
        except Decouverte.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        decouverte = self.get_object(pk)
        serializer = DecouverteSerializer(decouverte)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        decouverte = self.get_object(pk)
        decouverte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdresseList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Adresse.objects.all()

    def get(self, request, format=None):
        adresses = Adresse.objects.all()
        serializer = AdresseSerializer(adresses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        if "pays" not in request.data:
            request.data["pays"] = "belgique"
        Pays.objects.get_or_create(nom=request.data["pays"])
        serializer = AdresseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdresseDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Adresse.objects.all()

    def get_object(self, pk):
        try:
            return Adresse.objects.get(pk=pk)
        except Adresse.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        adresse = self.get_object(pk)
        serializer = AdresseSerializer(adresse)
        return Response(serializer.data)


class PaysList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Pays.objects.all()

    def get(self, request, format=None):
        pays = Pays.objects.all()
        serializer = PaysSerializer(pays, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaysDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Pays.objects.all()

    def get_object(self, pk):
        try:
            return Pays.objects.get(pk=pk)
        except Pays.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pays = self.get_object(pk)
        serializer = PaysSerializer(pays)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        pays = self.get_object(pk)
        pays.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()

    def get(self, request, format=None):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PhotoDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser | IsUser
    ]
    queryset = Photo.objects.all()

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo)  # noqa: F405
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PhotoListByDecouverte(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Photo.objects.all()

    def get(self, request, decouverte, format=None):
        photos = Photo.objects.all().filter(decouverte=decouverte)
        serializer = PhotoSerializer(photos, many=True)  # noqa: F405
        return Response(serializer.data)


class UnderMaintenance(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        personne = Personne.objects.get(username="maintenance")
        return Response({"maintenance": personne.hashtag})
