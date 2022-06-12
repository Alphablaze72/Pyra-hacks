import sqlite3
import math
import cs50
#the database is taken from IMDB

db = sqlite3.SQLITE_READ("sqlite:///shows.db")

def main():
    request = input('What whould like to search for(Movie or person: ')
    if request == 'Movie':
        movie_request = input("whioch movie would you likle information about: ")
        rows = db.execute("SELECT * FROM shows WHERE title LIKE ?", movie_request)
        for row in rows:
            print(row)
    if request == 'person':
        person_request = input("whioch person would you likle information about: ")
        rows = db.execute("SELECT * FROM people WHERE name LIKE ?", person_request)
        for row in rows:
            print(row)
            


