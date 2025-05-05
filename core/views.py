import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .services import fetch_champions, fetch_champion_detail

# Displays list of all champions
def champ_list(request):
    champions = fetch_champions() # Master data for all champions
    return render(request, "core/champ_list.html", {
        "champions": champions, #template context
    })

# This is detailed info for a single champion
def champ_detail(request, champ_key):
    champ = fetch_champion_detail(champ_key) # detailed data for a champion key
    return render(request, "core/champ_detail.html", {
        "champ": champ, #champion dictionary to detail template
    })

# I am using django built in form to handle user registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # posted data to form
        if form.is_valid(): # validation
            form.save() # create new User in DB
            return redirect("login") #Goes back to login page
    else:
        form = UserCreationForm() # empty form

    return render(request, "core/register.html", {"form": form})
# For random champion image and checking name, for the quiz
def quiz(request):
    champions = fetch_champions() #full champion list

    request.session.setdefault("quiz_score", 0) # Starting score


    if request.method == "POST":
        # User submitted an answer so must compare to the stored key, made it lower so it doesn't matter how you type it
        answer   = request.POST.get("answer", "").strip().lower()
        correct  = request.session.get("quiz_current_key", "").lower()
        if answer == correct:
            request.session["quiz_score"] += 1 # increment score on correct
            result = "Correct!"
        else:
            result = f"Wrong! It was {correct.title()}."
        request.session["quiz_feedback"] = result # feedback for next view
        return redirect("quiz") # Reload quiz page for next round

    # Pick a new champion for the quiz
    champ = random.choice(champions)
    # Save correct answer key
    request.session["quiz_current_key"] = champ["id"]

    return render(request, "core/quiz.html", {
        "champ": champ, #Champion dictionary  with image URL
        "score": request.session["quiz_score"],
        "feedback": request.session.pop("quiz_feedback", ""), #Popping feedback so it'll only show once
    })
