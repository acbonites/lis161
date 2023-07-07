from flask import Flask, render_template, request, redirect, url_for
from data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies/<genre>')
def movies(genre):
    films_list = read_films_by_genre(genre)
    return render_template("movies.html", genre=genre, films=films_list)

@app.route('/movies/<int:film_id>')
def movie(film_id):
    film = read_films_by_film_id(film_id)
    if film:
        return render_template("film.html", film=film)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/processed', methods=['post'])
def processing():
    film_data = {
        "genre": request.form['genre'],
        "title": request.form['film_title'],
        "year": request.form['film_year'],
        "cast": request.form['film_cast'],
        "director": request.form['film_director'],
        "summary": request.form['film_summary'],
        "url": request.form['film_url']
    }
    insert_film(film_data)
    return redirect(url_for('movies', genre=request.form['genre']))

@app.route('/modify', methods=['post'])
def modify():
    if request.form["modify"] == "edit":
        film_id = request.form["film_id"]
        film = read_films_by_film_id(film_id)
        return render_template('update.html', film=film)
    elif request.form["modify"] == "delete":
        film_id = request.form["film_id"]
        delete_film(film_id)
        return redirect(url_for('index'))

@app.route('/update', methods=['post'])
def update():
    film_data = {
        "genre": request.form['genre'],
        "title": request.form['film_title'],
        "year": request.form['film_year'],
        "cast": request.form['film_cast'],
        "director": request.form['film_director'],
        "summary": request.form['film_summary'],
        "url": request.form['film_url'],
        "film_id": request.form['film_id']  # Use 'film_id' as the key name
    }

    update_film(film_data)
    return redirect(url_for('movie', film_id=request.form['film_id']))

@app.route('/search', methods=['get'])
def search():
    query = request.args.get('query', '')
    results = search_film(query)
    return render_template('search.html', query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
