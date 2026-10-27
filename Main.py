"""
File: Main.py
Description: A module where the test code is run from.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
"""

from platform import Platform

#movie1 = Movie('Interstellar', 'Sci-Fi', 169)

#print(movie1.title)
#print(movie1.genre)
#print(movie1.duration)

#movie1.duration = 180
#print(movie1.duration)

#movie1.duration = -180
#print(movie1.duration)

#print(movie1)

platform = Platform()
print()
platform.new_user('Sally')
platform.new_user('Jaydon')
platform.new_user('Billy')
platform.new_user('Bob')
print()
platform.new_movie('Disaster Movie', 'Comedy', 97)
platform.new_movie('Interstellar', 'Sci-Fi', 169)
platform.new_movie('Up', 'Animation', 96)
platform.new_movie('The Shawshank Redemption', 'Drama', 142)
platform.new_movie('Avatar', 'Sci-Fi', 162)
#print()
#user = platform.find_user('Sally')
#movie = platform.find_movie('Interstellar')
#print()
#print(user.username)
#print(movie.title)
#print()
#print(platform.find_user('Bob'))
#print(platform.find_movie('Up'))

#platform.add_to_watchlist('Sally', 'Interstellar')
#platform.add_to_watchlist('Sally', 'Interstellar')
#platform.add_to_watchlist('Sally', 'Avatar')

#user.watch_movie('Avatar')
#movie.watch_movie('Avatar')

platform.add_to_watchlist('Sally', 'Interstellar')
print()
platform.watch_movie('Sally', 'Interstellar')
platform.watch_movie('Sally', 'Interstellar')
platform.watch_movie('Sally', 'Up')
platform.watch_movie('Sally', 'Avatar')
print()

platform.rate_movie('Sally', 'Avatar', 3)
platform.rate_movie('Sally', 'Up', 4)
platform.rate_movie('Sally', 'Up', 5)
platform.rate_movie('David', 'Avatar', 5)
platform.rate_movie('Sally', 'Up', -6)
print()

# Testing the __str__() method in the User, Platform and Movie classes.
user1 = platform.find_user('Sally')
movie1 = platform.find_movie('Disaster Movie')
print(user1)
print()
print(movie1)
print()
print(platform)
print()

# Testing user_summary and movie_summary.
platform.user_summary('Sally')
print()
platform.movie_summary('Avatar')

# Test rating system again.
print()
platform.watch_movie('Bob', 'Avatar')
platform.rate_movie('Bob', 'Avatar', 5)
print()
platform.movie_summary('Avatar')
print()

# More movie and user summary testing
platform.movie_summary('Disaster Movie')
print()

platform.user_summary('Billy')
print()

platform.rate_movie('Jaydon', 'Interstellar', 4)

# Testing duplicate addition of a user.
platform.new_user('Sally')

# Testing duplicate addition of a movie
platform.new_movie('Avatar', 'Sci-Fi', 162)

# Testing duplicate addition of a movie into a watchlist.
platform.add_to_watchlist('Billy', 'Interstellar')
platform.add_to_watchlist('Billy', 'Interstellar')

# Testing if watching a movie not on the platform works as intended.
platform.watch_movie('Sally', 'Titanic')

# Testing if rated movie appears as intended.
platform.user_summary('Bob')
print()

# Testing if non-existent movie correctly doesn't produce a summary.
platform.movie_summary('Titanic')