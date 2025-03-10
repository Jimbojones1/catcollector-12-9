from django.shortcuts import render, redirect

# importing of CBV (class based view)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView # add these 
from django.http import HttpResponse
# Create your views here.
from .models import Cat, Toy

from .forms import FeedingForm






# Other view functions above

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'



# controller FILE, in DJANGO we call them VIEW FUNCTIONS
# ALL THE VIEW FUNCTIONS GO IN THIS FILE

# reusing the main_app/cat_form template (same as create)
# but now the template has a cat variable or (object ) variable
# handling the get and put
class CatUpdate(UpdateView):
    model = Cat
    # disallow updating the name
    fields = ['breed', 'description', 'age']
    # this will use the get_absolute_url on the model to redirect
    # to the detail page after an update

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/' # redirect to the index because we just deleted the cat
    # there is no details anymore






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
    feeding_form = FeedingForm()# creates an instance of form

    # cats/detail.html should be in templates folder
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})
    

# cat_id comes from the params in urls.py file for the add_feeding
def add_feeding(request, cat_id):
    # create a modelForm instance with the data from the post request(form submission)
    # in express req.body, in django request.POST
    form = FeedingForm(request.POST)
    # validate the Form and add the cat_id to the form
    if form.is_valid():
        # create in memory instance (on the server)
        new_feeding = form.save(commit=False)
        # assign the cat_id to the form for the cat_id column in psql
        new_feeding.cat_id = cat_id
        # save it (Which adds the new row to the feeding table in psql)
        new_feeding.save()

   #import redirect at the top, cat_id on the left is the param name, right is value 
    return redirect('cats-detail', cat_id=cat_id)




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



