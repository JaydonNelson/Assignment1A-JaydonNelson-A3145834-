'''
File: movie.py
Description: A module where the Movie class is constructed.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Movie:
    def __init__(self, title, genre, duration):
        self.__movie_list = []
        self.__movie = {}
        self.__title = title
        self.__genre = genre
        self.__duration = duration
        self.__avg_rate = []

        pass
