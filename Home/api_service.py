from decouple import config
import http.client
import json


def search_title(title):
    API_KEY = config('API_KEY')

    conn = http.client.HTTPSConnection("imdb-internet-movie-database-unofficial.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

    # use of f string and replace method to get correct format for URL
    conn.request("GET", f"/search/{title.replace(' ', '')}", headers=headers)

    res = json.loads((conn.getresponse()).read().decode('utf-8'))
    return res['titles']


def get_details(film_id):
    API_KEY = config('API_KEY')

    conn = http.client.HTTPSConnection("imdb-internet-movie-database-unofficial.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

    conn.request("GET", f"/film/{film_id}", headers=headers)

    res = json.loads((conn.getresponse()).read().decode('utf-8'))
    print(res)
