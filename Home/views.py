from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm
from .models import Movie
from .api_service import search_title, get_details


def index(request):
    movie = SearchForm(request.POST or None)
    context = {
        'movie': movie,
        'results': [],
        'rating': []
    }
    if request.method == 'POST':
        if 'search_movies' in request.POST:
            search_results = api_request(request)
            for i in search_results:
                print(get_ratings(i['id']))
                if get_ratings(i['id']):
                    rating = get_object_or_404(Movie, pk=i['id'])
                    print(rating)
                context['results'].append(i)
            return render(request, 'Home/home.html', context)
        elif 'like' in request.POST:
            print(request.POST.get('like'))  # prints id of movie button clicked



            return redirect('Home:index')

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


def get_ratings(movie_id):
    movie = Movie.Movies.filter(pk=movie_id)
    if movie:
        rating = {
            'likes': movie.thumbsUp,
            'dislikes': movie.thumbsDown
        }
        return rating
    else:
        return False


def post_like():
    pass


def post_dislike():
    pass