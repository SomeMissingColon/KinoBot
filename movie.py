from builtins import enumerate
import random
import math

from parsing import Parsing


#TODO: gotta integrate user id to reviews
class Movie:
    def __init__(self, name, user_reviews, snaps):
        self.name = name.lower()
        self.user_reviews = user_reviews
        self.snaps = snaps
        self.update()

    def update(self):
        if not len(self.user_reviews) == 0:
            sum_ratings = 0
            for key, value in self.user_reviews.items():
                sum_ratings += value
            self.rating_average = sum_ratings / len(self.user_reviews)
        else:
            self.rating_average = "This movie has no review yet, use \"!rate moviename,Rating\" to change that!"
        self.imdb_rating = Parsing(self.name).get_rating()

    def user_rate(self, rating):
        rate_str = rating["rating"]
        try:
            rating["rating"] = float("%.1f" % float(rate_str))
        except:
            return None
        if not math.ceil(rating["rating"]) > 10 or math.ceil(rating["rating"]) < 0:
            self.user_reviews[rating["user_id"]] = rating["rating"]
            self.update()
            return self.rating_average
        return None

    def add_snap(self, link):
        if "imgur" in link:
            self.snaps.append(link)
            return "Snapshot successfully added"
        else:
            return None

    def to_hash(self):
        return {"name":self.name, "user_reviews":self.user_reviews, "snaps":self.snaps}

    def to_chat(self):
        output = "{0}:\nIMDB rating: {1}\nCommunity rating: {2}/10 out of {3} reviews\n".format(self.name, self.imdb_rating, self.rating_average,str(len(self.user_reviews)))
        if not len(self.snaps) == 0:
            output += self.snaps[random.randint(0,(len(self.snaps) - 1))]
        return output