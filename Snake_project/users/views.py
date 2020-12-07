from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Team
from django import forms
from .models import Person
from .forms import PersonForm


# Create your views here.

def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
        personForm = PersonForm()
    else:
        form = UserCreationForm(data = request.POST)
        personForm = PersonForm(data=request.POST)
        if form.is_valid()and personForm.is_valid():
            savedUser = form.save()
            person = personForm.save(commit=False);
            person.user = savedUser;
            person.score = 0;
            personForm.save();
            return redirect('users:login')
    context = {'form':form, 'person_form':personForm}
    return render(request, 'registration/register.html',context)
def teams(request): 
    teamsList = Team.objects.filter(userOwner = request.user).order_by('id')
    if forms.is_valid():
        new_team = form.save(commit=False) #not stored by db yet
        new_team.userOwner = request.user #add the user to FK
        return redirect('game:teams')
