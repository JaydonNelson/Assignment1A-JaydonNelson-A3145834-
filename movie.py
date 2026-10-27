"""
File: movie.py
Description: A module where the Movie class is constructed.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
"""

class Movie:
    def __init__(self, title, genre, duration):
        self.__title = title
        self.__genre = genre
        self.__duration = duration

    def get_title(self):
        return self.__title

    def get_genre(self):
        return self.__genre

    def get_duration(self):
        return self.__duration

    def set_title(self, title):
        if isinstance(title, str):
            self.__title = title

        else:
            print("Title must be a string.")

    def set_genre(self, genre):
        if isinstance(genre, str):
            self.__genre = genre

        else:
            print("Genre must be a string.")

    def set_duration(self, duration):
        if isinstance(duration, int) and duration > 0:
            self.__duration = duration

        else:
            print("Duration must be a integer above 0.")

    title = property(get_title, set_title)
    genre = property(get_genre, set_genre)
    duration = property(get_duration, set_duration)

    # Summarizes the movie object and displays its title, genre and duration.
    # Also used in movie_summary in Platform class.
    def movie_summary(self):
        print('-----------------')
        print()
        print(f'Title: {self.title}')
        print()
        print(f'Genre: {self.genre}')
        print()
        print(f'Duration: {self.duration}')
        print()

    def __str__(self):
        return f"{self.title} is a film in the {self.genre} genre"\
               f" with a duration of {self.duration} minutes."