from flask import Blueprint, jsonify, request
from flask_cors import CORS
from models.movie_model import MovieModel
from databases.movie_dabase import MovieDatabase

movies = Blueprint("movies", __name__)
CORS(movies, methods=["GET"])


def is_valid(arg):
    return arg is not None or arg != ""


@movies.route("/top_rated", methods=["GET"])
def top_rated_movies():
    page = request.args.get("page", default="")
    page = int(page) if is_valid(page) and page.isdigit() else 1
    if page <= 0:
        return (
            jsonify({"error": "page must be greater than 0", "success": "false"}),
            422,
        )
    db = MovieDatabase()
    movie_data = [
        MovieModel(
            title, vote_average, path_to_image, genres, length, description
        ).__dict__
        for title, vote_average, path_to_image, genres, length, description in db.get_top_rated_movies(
            page
        )
    ]
    db.close()
    return jsonify({"page": page, "results": movie_data}), 200


@movies.route("/popular", methods=["GET"])
def popular_movies():
    page = request.args.get("page", default="")
    page = int(page) if is_valid(page) and page.isdigit() else 1
    if page <= 0:
        return (
            jsonify({"error": "page must be greater than 0", "success": "false"}),
            422,
        )
    db = MovieDatabase()
    movie_data = [
        MovieModel(
            title, vote_average, path_to_image, genres, length, description
        ).__dict__
        for title, vote_average, path_to_image, _, genres, length, description in db.get_popular_movies(
            page
        )
    ]
    db.close()
    return jsonify({"page": page, "results": movie_data}), 200


@movies.route("/alphabetical", methods=["GET"])
def alphabetical_order_movies():
    page = request.args.get("page", default="")
    page = int(page) if is_valid(page) and page.isdigit() else 1
    if page <= 0:
        return (
            jsonify({"error": "page must be greater than 0", "success": "false"}),
            422,
        )
    db = MovieDatabase()
    movie_data = [
        MovieModel(
            title, vote_average, path_to_image, genres, length, description
        ).__dict__
        for title, vote_average, path_to_image, genres, length, description in db.get_alphabetical_movies(
            page
        )
    ]
    db.close()
    return jsonify({"page": page, "results": movie_data}), 200


@movies.route("/reverse_alphabetical", methods=["GET"])
def reverse_alphabetical_order_movies():
    page = request.args.get("page", default="")
    page = int(page) if is_valid(page) and page.isdigit() else 1
    if page <= 0:
        return (
            jsonify({"error": "page must be greater than 0", "success": "false"}),
            422,
        )
    db = MovieDatabase()
    movie_data = [
        MovieModel(
            title, vote_average, path_to_image, genres, length, description
        ).__dict__
        for title, vote_average, path_to_image, genres, length, description in db.get_reverse_aphabetical_movies(
            page
        )
    ]
    db.close()
    return jsonify({"page": page, "results": movie_data}), 200


@movies.route("/movies", methods=["GET"])
def movies_by_search():
    search = request.args.get("search")
    db = MovieDatabase()
    movie_data = [
        MovieModel(
            title, vote_average, path_to_image, genres, length, description
        ).__dict__
        for title, vote_average, path_to_image, genres, length, description in db.get_movies_by_search(
            search
        )
    ]
    db.close()
    return jsonify({"results": movie_data}), 200
