from django.shortcuts import render
from django.db import connection
from .models import Events
# Create your views here.
def base(request):
    
    events=Events.objects.all()
    return render(request, 'base.html',{'events':events})

