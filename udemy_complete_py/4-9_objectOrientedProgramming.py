# defining a method
# Define a Movie class that has two properties: name and director

class Movie:
    def __init__(self, new_name, new_director):
        self.name = new_name
        self.director = new_director

    def print_info(self):
        print("<<" + self.name + ">>" + " by " + self.director)

my_movie = Movie("The Matrix", "Wachowski")
print(my_movie.name)
print(my_movie.director)

my_movie.print_info()