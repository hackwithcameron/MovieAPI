from django.shortcuts import render
from .forms import SearchForm

def index(request):
    movie = SearchForm(request.POST or None)
    return render(request, 'Home/home.html')


def searchTitle(request, title):
    context = {
        'title': title
    }
    return render(request, 'Home/search.html', context)