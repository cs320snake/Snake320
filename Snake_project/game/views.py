from django.shortcuts import render

from .models import Match

from datetime import date

# Create your views here.
def home(request):
    if request.method == 'POST':    
        score = request.POST.get("scoreAttr");
        match = Match();
        match.user = request.user;
        match.date = date.today(); # need to add: from datetime import date
        match.score = score;
        match.save();
    return render(request, 'game/index.html')