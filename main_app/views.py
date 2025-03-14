from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
# importing of CBV (class based view)
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView # add these 
from django.http import HttpResponse
# Create your views here.
from .models import Cat, Toy

from .forms import FeedingForm

## AUTHORIZATION
from django.contrib.auth.decorators import login_required # function based views
from django.contrib.auth.mixins import LoginRequiredMixin # for CBVS

### Imports for the signup!
from django.contrib.auth import login # login function
from django.contrib.auth.forms import UserCreationForm # form instance for creating user


def signup(request):
    # view functions can handle multiple http requests
    error_message = ''
    # handle the post request (submission of the form)
    if request.method == "POST":
        # create a user form object that includes the data from the submitted form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # save the form and create the user 
            # adds a row to the user table
            user = form.save()
            # login in the user 
            login(request, user)
            # this creates the request.user ^ in all our view functions

            return redirect('cats-index') # cats-index is the name of a path in urls.py
        else: 
            error_message = "Invalid sign up - try again"
    # handling the get request 
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})


def remove_toy(request, cat_id, toy_id):
    # Look up the cat
    cat = Cat.objects.get(id=cat_id)
    # Look up the toy
    cat.toys.remove(toy_id)
    # Remove the toy from the cat
    return redirect('cats-detail', cat_id=cat.id)


# cat_id and toy_id match the params in urls.py
def associate_toy(request, cat_id, toy_id):
    # find the cat then add the toy_id to the cats toys
    cat = Cat.objects.get(id=cat_id)
    # creates the association
    cat.toys.add(toy_id)
    # optional one liner
    # Cat.objects.get(id=cat_id).toys.add(toy_id)
    return redirect('cats-detail', cat_id=cat_id)

# Other view functions above

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

# What template? templates/<name_of_the_app>/<model_name>_list.html
# templates/main_app/toy_list.html
# whats the variable for all toys in that template?
# <model_name>_list, object_list
# toy_list
class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy


class ToyUpdate(LoginRequiredMixin, UpdateView):
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
    fields = ['name', 'breed', 'description', 'age'] # '__all__ 'include all the keys on the Cat model in the form
    # success_url = '/cats/'
    def form_valid(self, form):
        # this is a place where you can add things to the form once it was submitted to the
        # server

        # assign the logged in user to the form (instance)that was submitted to the server
        form.instance.user = self.request.user # self.request.user is the logged in user! 
        # let the form add the new to the database now!
        return super().form_valid(form)


# cat_id comes from the route path (thats our param)
# path('cats/<int:cat_id>/', views.cat_detail, name='cats-detail'),
@login_required # decorator - just a function that is called right before another function (think middleware in express)
def cat_detail(request, cat_id):

    # use our model to find the row that matches cat_id in the params from 
    # cats table
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()# creates an instance of form

    # # Grab all the toys (Select all the rows from the toys table)
    # toys = Toy.objects.all()
    # grab all the toys the cat does not have
    # cat.toys.all().values_list('id') === [1, 3, 4]
    # django field looks ups <- google this for the syntax options
    toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))

    # cats/detail.html should be in templates folder
    return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form, 'toys': toys_cat_doesnt_have})
    

# cat_id comes from the params in urls.py file for the add_feeding
@login_required
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



@login_required
def cat_index(request):
    # injecting a cats variable whose value is the array of cats on line 25
    # 'cats/index.html, django is looking in the templates always! 
    # looking inside a cats folder(resource)/index.html

    # use e Cat model to get all the rows from the cats table!
    # show EVERYONES CATS

    # cats = Cat.objects.all()

    ### SHOW LOGGED IN USERS CATS
    # request.user is the logged in user
    # user in a key on the cats model
    cats = Cat.objects.filter(user=request.user)

    return render(request, 'cats/index.html', {'cats': cats})

# def home(request):

#     # HttpResponse is like res.send in Express
#     return render(request, 'home.html')

class Home(LoginView):
    # specify a template
    template_name = 'home.html'


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



