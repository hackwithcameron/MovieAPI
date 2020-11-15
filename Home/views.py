from django.shortcuts import render
from .forms import SearchForm
from .api_service import search_title, get_details


def index(request):
    movie = SearchForm(request.POST or None)
    context = {
        'movie': movie,
        'results': [],
    }
    if request.method == 'POST':
        search_results = api_request(request)
        for i in search_results:
            context['results'].append(i)
        return render(request, 'Home/home.html', context)
    return render(request, 'Home/home.html', context)


def details(request, film_id):
    details = get_details(film_id)
    context = {
        'details': details,
    }
    return render(request, 'Home/details.html', context)


def api_request(request):
    title = request.POST.get('search_movie', False)
    res = search_title(title)
    return res
