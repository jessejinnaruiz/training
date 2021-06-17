# your first python class
# Define a Movie class that has two properties: name and director

class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

my_movie = Movie("The Matrix", "Wachowski")
print(my_movie.name)
print(my_movie.director)