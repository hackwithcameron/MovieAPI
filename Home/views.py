from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
                if get_ratings(i['id']):
                    i['rating'] = get_ratings(i['id'])
                context['results'].append(i)
            print(context['results'])
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


def get_ratings(movie_id):
    if Movie.Movies.filter(pk=movie_id).exists():
        movie = Movie.Movies.get(pk=movie_id)
        rating = {
            'likes': movie.thumbsUp,
            'dislikes': movie.thumbsDown,
            'movie_id': movie_id,
        }
        return rating
    else:
        return False


def post_like(request):
    if request.is_ajax() and request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        movie_title = request.POST.get('movie_title')
        movie_likes = request.POST.get('likes')
        csrf_token = request.POST.get('csrfmiddlewaretoken')

        obj, created = Movie.Movies.update_or_create(
            pk=movie_id, defaults={'title': movie_title, 'thumbsUp': int(movie_likes) + 1})

        return HttpResponse(obj.thumbsUp)
    else:
        return HttpResponse('unsuccessful')


def post_dislike(request):
    if request.is_ajax() and request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        movie_title = request.POST.get('movie_title')
        movie_dislikes = request.POST.get('dislikes')

        obj, created = Movie.Movies.update_or_create(
            pk=movie_id, defaults={'title': movie_title, 'thumbsDown': int(movie_dislikes) + 1})

        return HttpResponse(obj.thumbsDown)
    else:
        return HttpResponse('unsuccessful')
