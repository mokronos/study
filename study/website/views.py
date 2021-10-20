from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

class NewTaskForm(forms.Form):
    text = forms.CharField(label="Input here...", max_lengh=100)


def home(request):
    return render(request, "website/home.html")

def create(request):
    return render(request, "website/create.html", {"form": NewTaskForm()})
