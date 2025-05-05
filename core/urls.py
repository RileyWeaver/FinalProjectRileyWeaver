from django.urls import path
from . import views

urlpatterns = [
    path("champs/",     views.champ_list,   name="champ_list"),

    path("champs/<str:champ_key>/", views.champ_detail, name="champ_detail"),

]
