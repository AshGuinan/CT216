from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from weather_app.models import WeatherData
from weather_app.forms import WeatherDataForm
from django.contrib.auth.decorators import login_required

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/search-form/")
    else:
        form=UserCreationForm()

    return render(request,
                  "registration/register.html",
                  {'form':form})

def welcome(request):
    return render(request,'welcome.html')
