from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# Create a router and register our viewsets with it.
urlpatterns = [
    path("personne", views.PersonneList.as_view()),
    path(r"personne/<str:pk>/", views.PersonneDetail.as_view()),
    path(r"calloux", views.CallouxList.as_view()),
    path(r"calloux/user/<str:personne>", views.CallouxListByUser.as_view()),
    path(
        r"calloux/detail/<str:personne>/<int:numero>",
        views.CallouxDetail.as_view(),
    ),
    path(r"calloux/id/<int:id>", views.CallouxById.as_view()),
    path(r"decouverte", views.DecouverteList.as_view()),
    path(
        r"decouverte/calloux/<str:personne>/<int:numero>",
        views.DecouverteListByCalloux.as_view(),
    ),
    path(r"decouverte/user/<str:personne>", views.DecouverteListByUser.as_view()),
    path(r"decouverte/detail/<int:pk>", views.DecouverteDetail.as_view()),
    path(r"adresse", views.AdresseList.as_view()),
    path(r"adresse/<str:pk>/", views.AdresseDetail.as_view()),
    path(r"pays", views.PaysList.as_view()),
    path(r"pays/<str:pk>/", views.PaysDetail.as_view()),
    path(r"photo", views.PhotoList.as_view()),
    path(r"photo/<int:pk>", views.PhotoDetail.as_view()),
    path(
        r"decouverte/photo/<int:decouverte>",
        views.PhotoListByDecouverte.as_view(),
    ),
    path(r"maintenance", views.UnderMaintenance.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
