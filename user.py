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
        print('-----------------')
        print()
        if movie not in self.__watchlist:
            self.__watchlist.append(movie)
            print(f'Movie {movie.title} added to {self.username}\'s watchlist.')
            print()
            print('-----------------')


        else:
            print(f'Movie {movie.title} already in {self.username}\'s watchlist.')
            print()
            print('-----------------')

    # Checks if movie has been watched by user, if it has, a message lets user know.
    # If it hasn't been watched by user, adds the movie to movies_watched list.
    # If the movie was also in watchlist, removes the movie from watchlist.
    def watch_movie(self, movie):
        print('-----------------')
        print()

        if movie not in self.__movies_watched:
            if movie in self.__watchlist:
                self.__watchlist.remove(movie)

            self.__movies_watched.append(movie)
            print(f'{self.username} watched {movie.title}.')
            print()
            print('-----------------')

        else:
            print(f'Movie {movie.title} has already been watched by {self.username}.')
            print()
            print('-----------------')

    # Checks if movie is in movies_watched list and if it is an integer between values 1 and 5 inclusive.
    # If it is, the movie rating is added to the rating dictionary for the user.
    def rate_movie(self, movie, rating):
        print('-----------------')
        print()

        if movie in self.__movies_watched:
            if isinstance(rating, int) and 1 <= rating <= 5:
                self.__ratings[movie.title] = rating
                print(f'{self.username} rated the movie {movie.title} {rating}/5.')
                print()
                print('-----------------')

            else:
                print('Rating must be an integer between 1 and 5.')
                print()
                print('-----------------')

        else:
            print(f'Movie {movie.title} has not been watched by {self.username} yet.')
            print()
            print('-----------------')

    # Displays a summary of a users watchlist, movies watched and ratings for rated movies.
    # If watchlist or movies watched are empty, it lets user know.
    def user_summary(self):
        print('-----------------')
        print()
        print(f'User: {self.username}')
        print()

        if len(self.__watchlist) > 0:
            print('Movies in watchlist:')

            for movie in self.__watchlist:
                print(f'- {movie.title}')
                print()

        else:
            print(f'No movies in {self.username}\'s watchlist.')
            print()

        print(f'Movies {self.username} has watched:')
        print()

        if len(self.__movies_watched) > 0:
            for movie in self.__movies_watched:
                if movie.title in self.__ratings:
                    rating = self.__ratings[movie.title]
                    print(f'- {movie.title} watched, rated {rating}/5')
                    print()

                else:
                    print(f'- {movie.title} watched, not rated.')
                    print()

            print()
            print('-----------------')

        else:
            print(f'No movies have been watched by {self.username}.')
            print()
            print('-----------------')

    # Returns the value for rating for a specific movie title.
    # If the user has not rated the movie, None is returned.
    def find_rating(self, title):
        return self.__ratings.get(title)

    def __str__(self):
        return f'User: {self.username}'




