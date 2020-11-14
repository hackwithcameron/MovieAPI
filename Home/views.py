from django.shortcuts import render
from .forms import SearchForm
from .api_service import search_title


def index(request):
    if request.method == 'POST':
        api_request(request)
    movie = SearchForm(request.POST or None)
    return render(request, 'Home/home.html')


def details(request):
    title = request.POST.get('title', False)
    context = {
        'title': title
    }
    return render(request, 'Home/details.html', context)


def api_request(request):
    title = request.POST.get('title', False)

    search_title(title)

    return render(request, 'Home/home.html')
