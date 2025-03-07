from django.shortcuts import render

# importing of CBV (class based view)
from django.views.generic.edit import CreateView

from django.http import HttpResponse
# Create your views here.
from .models import Cat

# controller FILE, in DJANGO we call them VIEW FUNCTIONS
# ALL THE VIEW FUNCTIONS GO IN THIS FILE







# handles both the GET AND POST request
class CatCreate(CreateView):
    # what model should this cbv use
    model = Cat
    # what inputs do you want to include on the form 
    # array of the keys on your model, which will be inputs on your form
    # fields = ['name', 'breed', 'description']
    fields = '__all__' # include all the keys on the Cat model in the form
    # success_url = '/cats/'


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

    # use e Cat model to get all the rows from the cats table!
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



