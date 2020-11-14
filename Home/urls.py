from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
]