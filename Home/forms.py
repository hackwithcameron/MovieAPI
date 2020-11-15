from .models import Movie
from django import forms


class SearchForm(forms.Form):
    search_movie = forms.CharField(max_length=100)

