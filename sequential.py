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

movie = {'title': 'Disaster Movie', 'genre': 'Comedy', 'duration': 97}
movie_list.append(movie)

movie = {'title': 'Lego: The Adventures of Clutch Powers', 'genre': 'Animation', 'duration': 78}
movie_list.append(movie)

# User list - Users name, movies in their watchlist, movies they have watched, any ratings they submitted.
user_list = []

user = {'username': 'Jaydon', 'watchlist':[], 'movies_watched':[], 'ratings':{}}
user_list.append(user)

user = {'username': 'Sally', 'watchlist':[], 'movies_watched':[], 'ratings':{}}
user_list.append(user)

user = {'username': 'Bob', 'watchlist':[], 'movies_watched':[], 'ratings':{}}
user_list.append(user)


def new_user(username):
    user_exists = False
    for user in user_list:
        if user['username'] == username:
            user_exists = True

        if user_exists == False:
            user = {'username': username, 'watchlist':[], 'movies_watched':[], 'ratings':{}}
            user_list.append(user)
            print(f'{username} added to users list')
    else:
        print('Username already exists')


def new_movie(title, genre, duration):
    movie_exists = False
    for movie in movie_list:
        if movie['title'] == title:
            movie_exists = True

    if movie_exists == False:
        movie = {'title': title, 'genre': genre, 'duration': duration}
        movie_list.append(movie)
        print(f'{title} added to movies list')
    else:
        print('Movie already exists')


def add_to_watchlist(username, title):
    user_exists = False
    movie_exists = False
    for user in user_list:
        if user['username'] == username:
            user_exists = True

            for movie in movie_list:
                if movie['title'] == title:
                    if title not in user['watchlist']:
                        if title in movie['title']:
                            user['watchlist'].append(title)
                            movie_exists = True
                            print(f'{title} added to watchlist for {username}')

                        else:
                            movie_exists = False
                            print(f'{title} not found on platform')

                    elif title in user['watchlist']:
                        movie_exists = True
                        print(f'{title} already exists in watchlist for {username}')

            if movie_exists == False:
                print(f'{title} not found on platform')

    if user_exists == False and movie_exists == True:
        print(f'User {username} not found on platform')

    elif user_exists == False and movie_exists == False:
        print(f'User {username} and movie {title} both not found on platform')


def watch_movie(username, title):
    user_exists = False
    movie_exists = False
    for user in user_list:
        if user['username'] == username:
            user_exists = True

            for movie in movie_list:
                if movie['title'] == title:
                    if title not in user['movies_watched']:
                        if title in movie['title']:
                            if title in user['watchlist']:
                                user['watchlist'].remove(title)
                            user['movies_watched'].append(title)
                            movie_exists = True
                            print(f'{title} watched by {username}')

                        else:
                            movie_exists = False
                            print(f'{title} not found on platform')

                    elif title in user['movies_watched']:
                        movie_exists = True
                        print(f'{title} has already been watched by {username}')

            if movie_exists == False:
                print(f'{title} not found on platform')

    if user_exists == False and movie_exists == True:
        print(f'User {username} not found on platform')

    elif user_exists == False and movie_exists == False:
        print(f'User {username} and movie {title} both not found on platform')


def rate_movie(username, title, rating):
    user_exists = False
    movie_exists = False

    for user in user_list:
        if user['username'] == username:
            user_exists = True

            for movie in movie_list:
                if movie['title'] == title:
                    if title in user['movies_watched']:
                        if movie['title'] == title:
                            if isinstance(rating, int):
                                if 0 <= rating <= 100:
                                    user['ratings'][title] = rating
                                    movie_exists = True
                                    print(f'{title} rated {rating}/100 by {username}')
                                else:
                                    print(f'{title} cannot be rated above 100 or below 0')

                            else:
                                movie_exists = False
                                print(f'{title} not found on platform')

                    elif title not in user['movies_watched']:
                        movie_exists = True
                        print(f'{title} rated hasn\'t been watched by {username} yet')

            if movie_exists == False:
                print(f'{title} not found on platform')

    if user_exists == False and movie_exists == True:
        print(f'User {username} not found on platform')

    elif user_exists == False and movie_exists == False:
        print(f'User {username} and movie {title} both not found on platform')


watch_movie('Sally', 'Disaster Movie')
print(user_list)
rate_movie('Sally', 'Disaster Movie', 80)
print(user_list)
rate_movie('Sally', 'Disaster Movie', 50)
print(user_list)




