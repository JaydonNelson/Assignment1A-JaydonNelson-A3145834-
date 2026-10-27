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
        self.__ratings = []


