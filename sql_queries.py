import sqlite3

conn = sqlite3.connect('HW/Artistc.db')
cursor = conn.cursor()

# *: select all features

#Question #1. How many artists are represented in the database? 
# num_artists = cursor.execute('''
#                 SELECT COUNT("Artist") FROM artists
#                              ''').fetchone()
# print(num_artists)

#Question #2. How many women (Female) are in the database?
# num_artists = cursor.execute('''
#                 SELECT COUNT("Artist ID") FROM artists WHERE Gender="Female"
#                              ''').fetchone()[0]
# print(num_artists)

#Question #3. How many people in the database were born before 1900?
# num_artists = cursor.execute('''
#                 SELECT COUNT("Artist ID") FROM artists WHERE "Birth Year"<1900
#                              ''').fetchone()[0]
# print(num_artists)

#Question #4*. What is the name of the oldest artist?
num_artists = cursor.execute('''
                SELECT "Name" FROM artists WHERE "Birth year"=(SELECT MIN("Birth Year") FROM artists)
                             ''').fetchone()[0]
print(num_artists)

