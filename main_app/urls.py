from django.urls import path
# import all the functions in views file
# as methods on a views object
from . import views

urlpatterns = [
    # localhost:8000, 
    # in the views folder we have home function
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cats-index'),
    # cat_id is the name of our param
    path('cats/<int:cat_id>/', views.cat_detail, name='cats-detail'),
    # allow render CBV's as_view()
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    # CBV expect the params name to be pk (primary key)
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    # 1 to many creation of a feeding (handling the post request from the feeding form)
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add-feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    #Existing urls above
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('cats/<int:cat_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate-toy'),

     
]