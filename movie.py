"""
File: movie.py
Description: A module where the Movie class is constructed.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Movie:
    def __init__(self, title, genre, duration):
        self.__movie_list = []
        self.__movie = {}
        self.__title = title
        self.__genre = genre
        self.__duration = duration
        self.__avg_rate = []

    def get_movie(self):
        return self.__movie

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_duration(self):
        return self.__duration

    def get_avg_rate(self):
        return self.__avg_rate

    def add_movie(self, movie):
        self.__movie_list.append(movie)
