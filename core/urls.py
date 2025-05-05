from django.urls import path
from . import views

urlpatterns = [

    path("",     views.champ_list,   name="champ_list"), #champion list url

    path("quiz/", views.quiz, name="quiz"), # quiz game url

    #url for details on specific champion, The <str:champ_key> is used to identify champion from the url
    path("<str:champ_key>/", views.champ_detail, name="champ_detail"),

]
