from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('',views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    path('search', views.search, name='search')
   
]