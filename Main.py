"""
File: Main.py
Description: A module where the test code is run from.
Author: Jaydon Nelson
Username: JaydonNelson
This is my own work as defined by the University's Academic Integrity Policy.
"""

from movie import Movie

movie1 = Movie('Interstellar', 'Sci-Fi', 169)

print(movie1.title)
print(movie1.genre)
print(movie1.duration)

movie1.duration = 180
print(movie1.duration)

movie1.duration = -180
print(movie1.duration)

print(movie1)