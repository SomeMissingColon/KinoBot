from movie import Movie
import json

#MOVIEREPO CONTAINS = name, ratings(like an array of votes), links(array of array containing the link and the report amount)

class MovieRepo:
    def __init__(self, path = "movie_list.json"):
        self.movies = []
        self.path = path
        self.load()
    def load(self):

        file = open(self.path, "r")

        try:
            self.json = json.loads(file.read())
        except:
            self.json = {}
        for key, value in self.json.items():
            name = value["name"]
            user_reviews = value["user_reviews"]
            snaps = value["snaps"]
            movie = Movie(name, user_reviews, snaps)
            self.movies.append(movie)
        file.close()

    def save(self):
        output = {}
        file = open(self.path, "w+")
        for movie in self.movies:
            output[movie.name] = movie.to_hash()
        file.write(json.dumps(output, separators=(",",":")))
        file.close()

    def add(self, movie):
        self.movies.append(movie)
        self.save()

    def remove(self, movie):
        self.movies.remove(movie)
        self.save(  )
    def find(self, movie_name):
        for movie in self.movies:
            if movie.name == movie_name.lower() :
                return movie
        return None
