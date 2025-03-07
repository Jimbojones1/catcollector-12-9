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
     
]