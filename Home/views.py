from django.http import HttpResponse
from django.shortcuts import render

from .forms import SearchForm
from .models import Movie
from .api_service import APIService


def index(request):
    """
    Main Home Page function. Returns searched movie on same page.
    """
    movie = SearchForm(request.POST or None)
    context = {
        'movie': movie,
        'results': [],
        'rating': []
    }
    if request.method == 'POST':
        if 'search_movies' in request.POST:  # Checks to see if the request includes 'search_movie'
            search_results = api_request(request)  # Gets info from API for movie search
            for i in search_results:  # looping through API results
                if get_ratings(i['id']):  # Checks to see if search result exists in db
                    i['rating'] = get_ratings(i['id'])
                context['results'].append(i)
            return render(request, 'Home/home.html', context)

    return render(request, 'Home/home.html', context)


def details(request, movie_id):
    """
    Gets Movie details by searching movie id with API
    """
    api = APIService()
    movie_details = api.get_details(movie_id)  # Gets movie details using movie unique ID
    context = {
        'details': movie_details,
    }
    return render(request, 'Home/details.html', context)


def api_request(request):
    """
    Returns response from API
    """
    api = APIService()
    title = request.POST.get('search_movie', False)  # Gets movie searched from request
    res = api.search_title(title)  # Searches API for movie using movie title
    return res


def get_ratings(movie_id):
    """
    Returns rating for movie if movie exists in db
    """
    if Movie.Movies.filter(pk=movie_id).exists():  # Checks db for existing movie entry to get likes and dislikes count
        movie = Movie.Movies.get(pk=movie_id)  # Gets likes and dislikes from db for movie
        rating = {
            'likes': movie.thumbsUp,
            'dislikes': movie.thumbsDown,
            'movie_id': movie_id,
        }
        return rating
    else:
        return False


def post_like(request):
    """
    Handles AJAX request for like button

    Returns Thumbs up count
    """
    if request.is_ajax() and request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        movie_title = request.POST.get('movie_title')
        movie_likes = request.POST.get('likes')

        obj, created = Movie.Movies.update_or_create(
            pk=movie_id, defaults={'title': movie_title, 'thumbsUp': int(movie_likes) + 1})

        return HttpResponse(obj.thumbsUp)
    else:
        return HttpResponse('unsuccessful')


def post_dislike(request):
    """
    Handles AJAX request for dislike button

    Returns Thumbs Down count
    """
    if request.is_ajax() and request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        movie_title = request.POST.get('movie_title')
        movie_dislikes = request.POST.get('dislikes')

        # Updates or creates db entry
        obj, created = Movie.Movies.update_or_create(
            pk=movie_id, defaults={'title': movie_title, 'thumbsDown': int(movie_dislikes) + 1})

        return HttpResponse(obj.thumbsDown)
    else:
        return HttpResponse('unsuccessful')
