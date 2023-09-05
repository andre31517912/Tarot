from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import TarotCard
from . models import gua

# Create your views here.
def home(request):
    return render(request, 'home.html')
def generate(request):
    random_cards = TarotCard.objects.order_by('?')[:3]  # Get 3 random cards
    context = {'cards': random_cards}
    return render(request, 'template.html', context)

def determineType(stro,word):
    type = ['sky','lake', 'fire', 'thunder','wind', 'water', 'mountain', 'ground']
    if stro == [1,1,1]:
        word.append(0)
    elif stro == [0,1,1]:
        word.append(1)
    elif stro == [1,0,1]:
        word.append(2)
    elif stro == [0,0,1]:
        word.append(3)
    elif stro == [1,1,0]:
        word.append(4)
    elif stro == [0,1,0]:
        word.append(5)
    elif stro == [1,0,0]:
        word.append(6)
    elif stro == [0,0,0]:
        word.append(7)
        
def determineFinal(words):
    #creating a 2d array from 1-64, 
    array_2d = []
    value = 1
    for _ in range(8):
        row = []
        for _ in range(8):
            row.append(value)
            value += 1
        array_2d.append(row)
    return array_2d[words[0]][words[1]]
    
def flipping(request):
    coin = [0,1]
    stroke = [] #results of coinflips, whether or not the stroke are full or half
    cstroke = [] #alternative result of coinflips. created to account for if coinflip results are MAJOR ying or MAJOR yang(in which case the strokes will interchanged from full to half vice versa)
    types = [] #each 3 strokes equates to a type, a list containing what the types of the 6 strokes will be ec. there will be 2 types from each read
    ctypes = [] #alternative types
    timeschanged = 0 #how many times we got MAJOR ying or MAJOR yang. this counter is used as an indicator to let the reader determine whether to read the original or alternative types, and which of the two types to read
    for x in range(6):
        horizontal = []
        for i in range(3):
            horizontal.append(random.randint(0,1))
        if horizontal.count(0) == 3:
            stroke.append(1)
            cstroke.append(0)
            timeschanged += 1 
        elif horizontal.count(0) == 2:
            stroke.append(1)
            cstroke.append(1)
        elif horizontal.count(0) == 1:
            stroke.append(0)
            cstroke.append(0)
        elif horizontal.count(0) == 0:
            stroke.append(0)
            cstroke.append(1)
            timeschanged += 1
        if len(stroke) == 3: 
            print("strokes/cstrokes:",stroke,cstroke)
            determineType(stroke,types)
            determineType(cstroke,ctypes)
            stroke = []
            cstroke = []
    context = {'number':determineFinal(types),
               'altnumber':determineFinal(ctypes),
               'timeschanged':timeschanged
               }
    return render(request, 'gua.html', context)