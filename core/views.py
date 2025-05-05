from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .services import fetch_champions, fetch_champion_detail

def champ_list(request):
    champions = fetch_champions()
    return render(request, "core/champ_list.html", {
        "champions": champions,
    })

def champ_detail(request, champ_key):
    champ = fetch_champion_detail(champ_key)
    return render(request, "core/champ_detail.html", {
        "champ": champ,
    })

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "core/register.html", {"form": form})