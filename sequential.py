'''
File: sequential.py
Description: A module for the sequential solution for the coastal streams online streaming platform.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
'''

# Movie list - Show all movies, which movies in which users watchlist, which movies each user watched, submitted ratings of movies.
# Movie summary - movie title, genre, duration and avg. user rating. included in dictionaries now.
movie_list = []

movie = {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'duration': 142}
movie_list.append(movie)

movie = {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'duration': 142}
movie_list.append(movie)

movie = {'title': 'Disaster Movie', 'genre': 'Comedy', 'duration': 97}
movie_list.append(movie)

movie = {'title': 'Lego: The Adventures of Clutch Powers', 'genre': 'Animation', 'duration': 78}
movie_list.append(movie)

# User list - Users name, movies in their watchlist, movies they have watched, any ratings they submitted.
user_list = []

user = {'username': 'Jaydon', 'watchlist':[]}
user_list.append(user)

user = {'username': 'Sally', 'watchlist':[]}
user_list.append(user)

user = {'username': 'Bob', 'watchlist':[]}
user_list.append(user)

def new_user(username):
    for user in user_list:
        if user['username'] != username:
            user = {'username': username, 'watchlist':[]}
            user_list.append(user)
        else:
            print('Username already exists')

def new_movie(title, genre, duration):
    for movie in movie_list:
        if movie['title'] != title:
            movie = {'title': title, 'genre': genre, 'duration': duration}
            movie_list.append(movie)
        else:
            print('Movie already exists')
