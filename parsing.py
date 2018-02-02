from bs4 import BeautifulSoup
import requests


class Parsing:
    def __init__(self, query):
        query.replace(" ", "+")
        self.url = "http://www.imdb.com/find?ref_=nv_sr_fn&q={0}&s=tt".format(query)
        self.html = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def get_movie_link(self):

        if self.soup.find(class_="result_text") is None:
            return False
        else:
            first_result = self.soup.find(class_="result_text").find("a")["href"]
            movie_link = "http://www.imdb.com" + first_result
            self.movie_html = requests.get(movie_link).text
            return True

    def get_rating(self):
        if self.get_movie_link():
            movie_soup = BeautifulSoup(self.movie_html, "html.parser")
            return movie_soup.find(class_="ratingValue").find("strong")["title"]
        else:
            return "Movie wasn't found on IMDB"

    def get_synopsis(self):
        if self.get_movie_link():
            movie_soup = BeautifulSoup(self.movie_html, "html.parser")
            return movie_soup.find(class_="plot_summary").find(class_="summary_text").text
        else:
            return "Movie wasn't found on IMDB"

