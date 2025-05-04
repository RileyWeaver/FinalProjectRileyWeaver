from django.shortcuts import render
from .services import fetch_champions

def champ_list(request):
    champions = fetch_champions()
    return render(request, "core/champ_list.html", {
        "champions": champions,
    })

def champ_detail(request, champ_id):
    champions = fetch_champions()
    champ = next(c for c in champions if c["id"] == champ_id)
    return render(request, "core/champ_detail.html", {"champ": champ})

