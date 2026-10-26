"""
File: sequential.py
Description: A module for the sequential solution for the coastal streams online streaming platform.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
"""

# Movie list - Show all movies, which movies in which users watchlist, which movies each user watched, submitted ratings of movies.
# Movie summary - movie title, genre, duration and avg. user rating. included in dictionaries now.
movie_list = []

movie1 = {'title': 'The Shawshank Redemption', 'genre': 'Drama', 'duration': 142}
movie_list.append(movie1)

movie2 = {'title': 'Disaster Movie', 'genre': 'Comedy', 'duration': 97}
movie_list.append(movie2)

movie3 = {'title': 'Lego: The Adventures of Clutch Powers', 'genre': 'Animation', 'duration': 78}
movie_list.append(movie3)

movie4 = {'title': 'Up', 'genre': 'Animation', 'duration': 96}
movie_list.append(movie4)

# User list - Users name, movies in their watchlist, movies they have watched, any ratings they submitted.
user_list = []

user1 = {'username': 'Jaydon', 'watchlist':[], 'movies_watched':[], 'ratings':{}}
user_list.append(user1)

user2 = {'username': 'Sally', 'watchlist':[], 'movies_watched':[], 'ratings':{}}
user_list.append(user2)

user3 = {'username': 'Bob', 'watchlist':[], 'movies_watched':[], 'ratings':{}}
user_list.append(user3)


# The function new_user(username) takes a users name and, unless they are already in the user_list, adds a user dictionary for said user.
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


# The function new_movie(title, genre, duration) takes a movies, title, genre and duration and, unless the title is already present in movie_list, adds the movie to movie_list as a movie dictionary.
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


# The function add_to_watchlist(username, title) takes a username and title and if both the user is in the user_list and title is in the movie_list, it adds the movie to said users watchlist
def add_to_watchlist(username, title):
    user_exists = False
    movie_exists = False
    for user in user_list:
        if user['username'] == username:
            user_exists = True

            for movie in movie_list:
                if movie['title'] == title:
                    if title not in user['watchlist']:
                        user['watchlist'].append(title)
                        movie_exists = True
                        print(f'{title} added to watchlist for {username}')

                    elif title in user['watchlist']:
                        movie_exists = True
                        print(f'{title} already exists in watchlist for {username}')

            if movie_exists == False:
                print(f'{title} not found on platform')

    if user_exists == False and movie_exists == True:
        print(f'User {username} not found on platform')

    elif user_exists == False and movie_exists == False:
        print(f'User {username} and movie {title} both not found on platform')


# The function watch_movie(username, title) takes a username and title and, if both are within their respective user_list and movie_list, adds the movie to the users movies_watched list. If it was in their watchlist, it is removed from there.
def watch_movie(username, title):
    user_exists = False
    movie_exists = False
    for user in user_list:
        if user['username'] == username:
            user_exists = True

            for movie in movie_list:
                if movie['title'] == title:
                    movie_exists = True

                    if title not in user['movies_watched']:
                        if title in user['watchlist']:
                            user['watchlist'].remove(title)

                        user['movies_watched'].append(title)
                        print(f'{title} watched by {username}')

                    elif title in user['movies_watched']:
                        print(f'{title} has already been watched by {username}')

            if movie_exists == False:
                print(f'{title} not found on platform')

    if user_exists == False and movie_exists == True:
        print(f'User {username} not found on platform')

    elif user_exists == False and movie_exists == False:
        print(f'User {username} and movie {title} both not found on platform')


# The function rate_movie(username, title, rating) takes a username, title of movie and rating of said movie (1-5).
# Adds the movie title as a key and the rating as a value in the ratings dictionary in the user dictionary.
# The function also adds the rating to the avg_rate list in the movie dictionary.
def rate_movie(username, title, rating):
    user_exists = False
    movie_exists = False

    for user in user_list:
        if user['username'] == username:
            user_exists = True

            for movie in movie_list:
                if movie['title'] == title:
                    movie_exists = True

                    if title in user['movies_watched']:
                        if isinstance(rating, int) and 1 <= rating <= 5:
                            user['ratings'][title] = rating
                            movie_exists = True
                            print(f'{title} rated {rating}/5 by {username}')

                        else:
                            print(f'{title} rating must be an integer and cannot be above 5 or below 1.')

                    elif title not in user['movies_watched']:
                        movie_exists = True
                        print(f'{title} has not been watched by {username} yet')

            if movie_exists == False:
                print(f'{title} not found on platform')

    if user_exists == False:
        print(f'User {username} not found on platform')


def user_summary(username):
    user_exists = False

    for user in user_list:
        if user['username'] == username:
            user_exists = True
            print(f'User: {username}')
            print()
            print('Movies in watchlist:')

            if len(user['watchlist']) > 0:
                for movie in user['watchlist']:
                    print(f'- {movie}')

            else:
                print(f'No movies in {username}\'s watchlist')

            print()
            print(f'Movies {username} has watched:')

            if len(user['movies_watched']) > 0:
                for movie in user['movies_watched']:
                    if movie in user['ratings']:
                        rating = user['ratings'][movie]
                        print(f'- {movie}, rated {rating}/5')

                    else:
                        print(f'{movie} has not been rated by {username}')

            else:
                print(f'No movies have been watched by {username}')

            print()
    if user_exists == False:
            print(f'User {username} not found on platform')


def movie_summary(title):
    movie_exists = False
    total_rate = 0
    people_rate = 0

    for movie in movie_list:
        if movie['title'] == title:
            movie_exists = True
            print('-----------------')
            print()
            print(f'Movie: {title}')
            print()
            print(f"Genre: {movie['genre']}")
            print()
            print(f"Duration: {movie['duration']} minutes")
            print()

            for user in user_list:
                if title in user['ratings']:
                    people_rate += 1
                    total_rate += user['ratings'][title]

            if people_rate > 0:
                avg_rating = total_rate / people_rate
                print(f"Average Rating: {avg_rating:.2f}/5")
                print()
                print('-----------------')
                print()
            else:

                print(f"No ratings available for {title}")
                print()
                print('-----------------')
                print()


    if movie_exists == False:
        print(f'Movie {title} not found on platform')
        print()
        print('-----------------')
        print()

add_to_watchlist('Sally', 'The Shawshank Redemption')
add_to_watchlist('Sally', 'Up')
watch_movie('Sally', 'Disaster Movie')
rate_movie('Sally', 'Disaster Movie', 4)
rate_movie('Sally', 'Up', 3)

watch_movie('Bob', 'Disaster Movie')
rate_movie('Bob', 'Disaster Movie', 3)
rate_movie('Bob', 'Disaster Movie', 2)
#print()
#print()
#print(movie_list)
#print()
#print(user_list)
#print()
#movie_summary('Disaster Movie')

# Testing if creates new user and rejects already existing user after.
new_user('Billy')
new_user('Billy')

# Testing that new movie function creates a new movie and if a duplicate is entered, it is rejected.
new_movie('Marmaduke','Family',87)
new_movie('Marmaduke','Family',87)

# Testing that watch movie function puts movie watched in movies_watched, add_to_watchlist adds movies to watchlist and that if a movie from the watchlist is watched, it is removed from watchlist and put in movies_watched list.
watch_movie('Billy','Marmaduke')
add_to_watchlist('Billy','Up')
print(user_list)
watch_movie('Billy','Up')

# Testing that rate_movie function adds rating for movie key as value in ratings dictionary, if not an integer between 1 and 5, it is rejected and if a new appropriate rating is made, the rating is updated for the user.
# If the user hasn't watched the movie yet, it should reject the rating attempt and notify the user.
rate_movie('Billy','Up',4)
rate_movie('Billy','Up',4.5)
rate_movie('Billy','Up',5)
rate_movie('Billy','The Shawshank Redemption',5)

print(user_list)
print(movie_list)

# Testing user_summary correctly summarizes only users who are within the user_list.
user_summary('Billy')
user_summary('Sally')
user_summary('Sam')

# Testing that movie_summary correctly summarizes only movies which are within the movie_list.
movie_summary('Up')
movie_summary('Disaster Movie')
movie_summary('Toy Story')




