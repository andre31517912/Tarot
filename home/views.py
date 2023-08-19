from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import TarotCard

# Create your views here.
def home(request):
    return render(request, 'home.html')
def generate(request):
    random_cards = TarotCard.objects.order_by('?')[:3]  # Get 3 random cards
    context = {'cards': random_cards}
    return render(request, 'template.html', context)