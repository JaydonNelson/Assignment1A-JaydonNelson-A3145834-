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
platform.new_user('Sally')
platform.new_movie('Interstellar', 'Sci-Fi', 169)
platform.new_movie('Up', 'Animation', 96)
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