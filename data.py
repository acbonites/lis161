import sqlite3

db_path = "md.db"

def connect_to_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_films_by_genre(genre):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM films WHERE genre = ?'
    value = genre
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_films_by_film_id(film_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM films WHERE id = ?'
    value = film_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result

def insert_film(film_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO films (genre, title, year, cast, director, summary, url) VALUES (?,?,?,?,?,?,?)'
    values = (film_data['genre'], film_data['title'], film_data['year'], 
              film_data['cast'], film_data['director'], film_data['summary'], 
              film_data['url'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def update_film(film_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE films SET genre=?, title=?, year=?, cast=?, director=?, summary=?, url=? WHERE id=?"
    values = (film_data['genre'], film_data['title'], film_data['year'], 
              film_data['cast'], film_data['director'], film_data['summary'], 
              film_data['url'], film_data['film_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_film(film_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM films WHERE id = ?"
    values = (film_id)
    cur.execute(query, values)
    conn.commit()
    conn.close()

def search_film(query):
    conn, cur = connect_to_db(db_path)
    sql_query = "SELECT * FROM films WHERE genre LIKE ? OR title LIKE ?"
    value = "%{}%".format(query)
    results = cur.execute(sql_query, (value, value)).fetchall()
    conn.close()
    return results
