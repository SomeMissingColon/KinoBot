import repo
from movie import Movie

class Controller:
    def __init__(self):
        self.repository = repo.MovieRepo()
    def create(self,name):
        if self.repository.find(name) is None:
            movie = Movie(name, {}, [])
            self.repository.add(movie)
            return "Movie successfully added"
        else:
            return "Movie already in database"
    def delete(self, movie_name):
        movie = self.repository.find(movie_name)
        if not movie == None:
            self.repository.remove(movie)
            return "Movie successfully Deleted"
        else:
            return "Movie is not in the database, check spelling"
    def get_movie(self, movie_name):
        movie = self.repository.find(movie_name)
        if not movie == None:
            movie.update()
            return movie.to_chat()
        else:
            return "Movie not in database, add it with !addMovie"
    def rate(self, movie_name, user_id, rating):
        error_message = "Invalid rating or the movie is not in the database\n Command usage: \"!rate <movie name>,<rating from 0.0 to 10.0>\""
        movie = self.repository.find(movie_name)
        rate = {"user_id":user_id, "rating":rating}
        if not movie == None:
            average_rating = movie.user_rate(rate)
            if average_rating == None:
                return error_message
            else:
                self.repository.save()
                return str(average_rating)
        else:
            return error_message

    def add_snap(self,movie_name,snap):
        error_message = "Invalid link or the movie is not in the database\nCommand usage: \"!addSnap <movie name>,<imgur link>\""
        movie = self.repository.find(movie_name)
        print(movie.name)
        if not movie == None:
            return_message = movie.add_snap(snap)
            if not return_message == None:
                return return_message
        else:
            return error_message
