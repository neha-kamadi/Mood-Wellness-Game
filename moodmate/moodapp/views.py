
# Create your views here.
from django.shortcuts import render, redirect
from .models import MoodHistory
import random
from collections import Counter

QUESTIONS = [
    ("You feel energetic in the morning?", 10),
    ("You often feel worried or overthink?", -10),
    ("You smile or laugh at small things?", 15),
    ("You prefer staying alone lately?", -5),
    ("You enjoy music or creative activities?", 10),
    ("You get angry quickly?", -10),
    ("You feel calm after deep breathing or yoga?", 15)
]

ACTIVITIES = {
    "Happy": ["Play your favorite upbeat song 🎵", "Go out with friends 😄", "Dance a little! 💃"],
    "Stressed": ["Try deep breathing 🧘", "Listen to soft instrumental music 🎶", "Take a short walk 🌿"],
    "Sad": ["Listen to cheerful songs 🎧", "Write about your feelings ✍️", "Talk to a close friend 💬"],
    "Calm": ["Do yoga or meditation 🧘‍♀️", "Practice gratitude 🙏", "Enjoy nature 🌸"],
  
  
}

def home(request):
    return render(request, "index.html")

def quiz(request):
    if request.method == "POST":
        name = request.POST["name"]
        random.shuffle(QUESTIONS)
        return render(request, "quiz.html", {"name": name, "questions": QUESTIONS})
    return redirect("home")

def result(request):
    if request.method == "POST":
        name = request.POST["name"]
        score = 0

        for i, (q, pts) in enumerate(QUESTIONS):
            ans = request.POST.get(f"q{i}")
            if ans == "yes":
                score += pts

        # Determine mood
        if score >= 40:
            mood = "Happy"
        elif 20 <= score < 40:
            mood = "Calm"
        elif 0 <= score < 20:
            mood = "Stressed"
        else:
            mood = "Sad"

        MoodHistory.objects.create(name=name, score=score, mood=mood)
        activities = ACTIVITIES[mood],
        return render(request, "result.html", {
            "name": name, "score": score, "mood": mood, "activities": activities, 
        })
    return redirect("home")

#count chart
def history(request):
    moods = MoodHistory.objects.all().order_by('-date')
    mood_counts = Counter(m.mood for m in moods)
    labels = list(mood_counts.keys())
    data = list(mood_counts.values())
    return render(request, "history.html", {
        "moods": moods,
        "labels": labels,
        "data": data
    })



