from django.urls import path
from . import views

urlpatterns = [
    path("",     views.champ_list,   name="champ_list"),

    path("quiz/", views.quiz, name="quiz"),

    path("<str:champ_key>/", views.champ_detail, name="champ_detail"),

]
