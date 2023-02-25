from flask import Blueprint, jsonify, request, g, abort
from flask_cors import CORS
from models.movie_model import MovieModel
from databases.movie_dabase import MovieDatabase

movies = Blueprint("movies", __name__)
CORS(movies, methods=["GET"])


@movies.before_request
def connect_database():
    g.db = MovieDatabase()


@movies.after_request
def close_database(response):
    if "db" in g:
        g.db.close()
    return response


def validate_page():
    page = request.args.get("page", default="")
    try:
        page = int(page)
        if page <= 0:
            abort(400, "Page should be greater than zero.")
        g.page = page
    except ValueError:
        abort(400, "Page should be an integer.")


def movie_response(get_movies):
    movie_data = [
        MovieModel(
            title, vote_average, path_to_image, genres, length, description
        ).__dict__
        for title, vote_average, path_to_image, _, genres, length, description in get_movies(
            g.page
        )
    ]
    return jsonify({"page": g.page, "results": movie_data}), 200


@movies.route("/top_rated", methods=["GET"])
def top_rated_movies():
    validate_page()
    return movie_response(g.db.get_top_rated_movies)


@movies.route("/popular", methods=["GET"])
def popular_movies():
    validate_page()
    return movie_response(g.db.get_popular_movies)


@movies.route("/alphabetical", methods=["GET"])
def alphabetical_order_movies():
    validate_page()
    return movie_response(g.db.get_alphabetical_movies)


@movies.route("/reverse_alphabetical", methods=["GET"])
def reverse_alphabetical_order_movies():
    validate_page()
    return movie_response(g.db.get_reverse_aphabetical_movies)


@movies.route("/movies", methods=["GET"])
def movies_by_search():
    search = request.args.get("search")
    movie_data = [
        MovieModel(
            title, vote_average, path_to_image, genres, length, description
        ).__dict__
        for title, vote_average, path_to_image, genres, length, description in g.db.get_movies_by_search(
            search
        )
    ]
    return jsonify({"results": movie_data}), 200
