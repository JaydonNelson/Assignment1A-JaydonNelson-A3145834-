"""
File: platform.py
Description: A module where the Platform class is constructed.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
"""

from user import User
from movie import Movie


class Platform:
    def __init__(self):
        self.__movie_list = []
        self.__user_list = []


    # Checks through movie_list and if the title is present for a movie, the function returns False, otherwise, returns True.
    def movie_exists(self, title):
        movie_exists = False

        for movie in self.__movie_list:
            if movie.title == title:
                movie_exists = True

        return movie_exists


    # Checks through user_list and if the username is present for a user, the function returns False, otherwise, returns True
    def user_exists(self, username):
        user_exists = False

        for user in self.__user_list:
            if user.username == username:
                user_exists = True

        return user_exists


    # Looks for user in user_list, if it finds user with username matching, it returns said user, if not, returns None.
    def find_user(self, username):
        for user in self.__user_list:
            if user.username == username:
                return user

        return None

    # Looks for movie in movie_list, if it finds movie with title matching, it returns said movie, if not, returns None.
    def find_movie(self, title):
        for movie in self.__movie_list:
            if movie.title == title:
                return movie

        return None


    # Adds a new user provided the username is not already present within the user_list, if it is, the user is notified.
    def new_user(self, username):
        if self.user_exists(username) == True:
            print(f'{username} already exists')

        else:
            self.__user_list.append(User(username))
            print(f'{username} added to users list')


    # Adds a new movie provided the title is not already present within the movie_list, if it is, the user is notified.
    def new_movie(self, title, genre, duration):
        if self.movie_exists(title) == True:
            print(f'{title} already exists')

        else:
            self.__movie_list.append(Movie(title, genre, duration))
            print(f'{title} added to movies list')

    # Finds user and movie and if both values are not None, it uses the add_to_watchlist method in User class to check if already in user's watchlist.
    # If it isn't it adds the movie, if it is, then it doesn't add it and prints message that it is already in watchlist.
    def add_to_watchlist(self, username, title):
        user = self.find_user(username)
        movie = self.find_movie(title)

        if user is not None and movie is not None:
            user.add_to_watchlist(movie)

        else:
            print(f'{username} or {movie} doesn\'t exist on platform.')

    # Finds user and movie and if both are not None in value through find_user and find_movie methods.
    # The watch_movie method in User class is used to check if movie has been watched before, if it hasn't, it is added to the movies_watched list.
    def watch_movie(self, username, title):
        user = self.find_user(username)
        movie = self.find_movie(title)

        if user is not None and movie is not None:
            user.watch_movie(movie)

        else:
            print(f'{username} or {title} doesn\'t exist on platform.')


    # Finds user and movie and if both are not None in value through find_user and find_movie methods.
    # The rate_movie method in User class is used to check if the movie has been watched, if it has, the rating is applied to said movie.
    # If the movie has been rated previously, the old rating will be replaced by the new rating.
    def rate_movie(self, username, title, rating):
        user = self.find_user(username)
        movie = self.find_movie(title)

        if user is not None and movie is not None:
            user.rate_movie(movie, rating)

        else:
            print(f'{username} or {movie} doesn\'t exist on platform.')



    def __str__(self):
        pass

