"""
File: user.py
Description: A module where the User class is constructed.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
"""

class User:
    def __init__(self, username):
        self.__username = username
        self.__watchlist = []
        self.__movies_watched = []
        self.__ratings = {}


    def get_username(self):
        return self.__username


    username = property(get_username)


    # Checks if movie is present in watchlist, if not, it adds it, if it is, then it alerts user it already is.
    def add_to_watchlist(self, movie):
        if movie not in self.__watchlist:
            self.__watchlist.append(movie)
            print(f'Movie {movie.title} added to watchlist.')

        else:
            print(f'Movie {movie.title} already in watchlist.')


    # Checks if movie has been watched by user, if it has, a message lets user know.
    # If it hasn't been watched by user, adds the movie to movies_watched list.
    # If the movie was also in watchlist, removes the movie from watchlist.
    def watch_movie(self, movie):
        if movie not in self.__movies_watched:
            if movie in self.__watchlist:
                self.__watchlist.remove(movie)

            self.__movies_watched.append(movie)
            print(f'{self.username} watched {movie.title}.')

        else:
            print(f'Movie {movie.title} has already been watched by {self.username}.')



    # Checks if movie is in movies_watched list and if it is an integer between values 1 and 5 inclusive.
    # If it is, the movie rating is added to the rating dictionary for the user.
    def rate_movie(self, movie, rating):
        if movie in self.__movies_watched:
            if isinstance(rating, int) and 1 <= rating <= 5:
                self.__ratings[movie.title] = rating
                print(f'{self.username} rated the movie {movie.title} {rating}/5.')

            else:
                print('Rating must be an integer between 1 and 5.')

        else:
            print(f'Movie {movie.title} has not been watched by {self.username} yet.')


    def __str__(self):
        pass




