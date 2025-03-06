from django.urls import path
# import all the functions in views file
# as methods on a view object
from . import views

urlpatterns = [
    # localhost:8000, 
    # in the views folder we have home function
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cats-index'),
]