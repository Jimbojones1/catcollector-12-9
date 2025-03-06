from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import Cat

# controller FILE, in DJANGO we call them VIEW FUNCTIONS
# ALL THE VIEW FUNCTIONS GO IN THIS FILE

# cat_id comes from the route path (thats our param)
# path('cats/<int:cat_id>/', views.cat_detail, name='cats-detail'),
def cat_detail(request, cat_id):

    # use our model to find the row that matches cat_id in the params from 
    # cats table
    cat = Cat.objects.get(id=cat_id)

    # cats/detail.html should be in templates folder
    return render(request, 'cats/detail.html', {'cat': cat})
    



def cat_index(request):
    # injecting a cats variable whose value is the array of cats on line 25
    # 'cats/index.html, django is looking in the templates always! 
    # looking inside a cats folder(resource)/index.html

    # use the Cat model to get all the rows from the cats table!
    cats = Cat.objects.all()

    return render(request, 'cats/index.html', {'cats': cats})

def home(request):

    # HttpResponse is like res.send in Express
    return render(request, 'home.html')


def about(request):
    # django knows to look for about.html
    # in a templates folder in our app
    return render(request, 'about.html')





















# ==================================================
# ==================================================
# FIRST DAY WE WILL USE A CLASS INSTEAD OF OUR MODEL
# to simulate some data
# views.py

# class Cat:
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age

# # Create a list of Cat instances
# cats = [
#     Cat('Lolo', 'tabby', 'Kinda rude.', 3),
#     Cat('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
#     Cat('Fancy', 'bombay', 'Happy fluff ball.', 4),
#     Cat('Bonk', 'selkirk rex', 'Meows loudly.', 6)
# ]
# ==================================================
# ==================================================



