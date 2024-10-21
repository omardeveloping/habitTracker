from django.shortcuts import render
from datetime import datetime
from calendar import monthrange

# Create your views here.

def index(request):
    current_date = datetime.now()
    date = current_date.date()
    letras = []

    days = monthrange(current_date.year, current_date.month)
    for i in range(1,days[1]):
        letras.append("a")

    data = {
        "date": date,
        "days": days[1],
        "letras": letras,
    }
    return render(request, "habits.html", data)