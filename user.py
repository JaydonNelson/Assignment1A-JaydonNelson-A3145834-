'''
File: user.py
Description: A module where the User class is constructed.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
'''

class User:
    def __init__(self, name):
        self.__user = {}
        self.__name = name
        self.__watchlist = []
        self.__watched = []
        self.__ratings = {}
        self.__userlist = []

    def get_name(self):
        return self.__name

    def get_watchlist(self):
        return self.__watchlist

    def get_watched(self):
        return self.__watched

    def set_watchlist(self, watchlist):
        self.__watchlist = watchlist

    def set_watched(self, watched):
        self.__watched = watched


    name = property(get_name)
    watchlist = property(get_watchlist)
    watched = property(get_watched)

