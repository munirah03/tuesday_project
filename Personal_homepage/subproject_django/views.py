from django.shortcuts import render
from Members.models import Members;

# Create your views here.

def index(request):
    context = {
        'firstname': 'Munirah',
        'age': 20,
    }
    return render (request,"index.html",context)

def testing(request):
    mymembers = Members.objects.all().values()
    context = {
        'mymembers' : mymembers,
    }
    return render (request, "index.html",context)