import random
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

import random
from django.shortcuts import render, redirect
from .services import fetch_champions

def quiz(request):
    champions = fetch_champions()
    # Initialize score in session
    request.session.setdefault("quiz_score", 0)

    if request.method == "POST":
        # Check previous answer
        answer   = request.POST.get("answer", "").strip().lower()
        correct  = request.session.get("quiz_current_key", "").lower()
        if answer == correct:
            request.session["quiz_score"] += 1
            result = "Correct!"
        else:
            result = f"Wrong! It was {correct.title()}."
        request.session["quiz_feedback"] = result
        return redirect("quiz")

    # GET: pick a random champ
    champ = random.choice(champions)
    # store its key for POST checking
    request.session["quiz_current_key"] = champ["id"]

    return render(request, "core/quiz.html", {
        "champ": champ,
        "score": request.session["quiz_score"],
        "feedback": request.session.pop("quiz_feedback", ""),
    })
