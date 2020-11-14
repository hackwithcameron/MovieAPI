from decouple import config
import http.client


def search_title(title):
    API_KEY = config('API_KEY')

    conn = http.client.HTTPSConnection("imdb-internet-movie-database-unofficial.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }

    # use of f string and replace method to get correct format for URL
    conn.request("GET", f"/search/{title.replace(' ', '')}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))
