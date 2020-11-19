from django.urls import path
from . import views

app_name = 'Home'
urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
    path('ajax/like/', views.post_like, name='post_like'),
    path('ajax/dislike/', views.post_dislike, name='post_dislike'),

]