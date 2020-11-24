from decouple import config
import http.client
import json


class APIService:
    def __init__(self):
        API_KEY = config('API_KEY')
        self.conn = http.client.HTTPSConnection("imdb-internet-movie-database-unofficial.p.rapidapi.com")

        self.headers = {
            'x-rapidapi-key': API_KEY,
            'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com"
        }

    def search_title(self, title):
        # use of f string and replace method to get correct format for URL
        self.conn.request("GET", f"/search/{title.replace(' ', '')}", headers=self.headers)

        res = json.loads((self.conn.getresponse()).read().decode('utf-8'))
        return res['titles']

    def get_details(self, film_id):
        # use of f string and replace method to get correct format for URL
        self.conn.request("GET", f"/film/{film_id}", headers=self.headers)

        res = json.loads((self.conn.getresponse()).read().decode('utf-8'))
        return res
