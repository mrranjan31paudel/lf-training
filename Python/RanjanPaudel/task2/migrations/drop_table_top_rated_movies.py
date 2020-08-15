import sqlite3

imdb_movies_db = 'sqlite_dbs/imdb_movies.db'

connection = sqlite3.connect(imdb_movies_db)
connection.execute('DROP TABLE top_rated_movies')
connection.commit()
connection.close()
