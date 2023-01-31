import logging
import click
from movieclub.themoviedb import TheMovieDB

@click.group()
@click.version_option()
def cli():
    """movie club test"""

@cli.command()
@click.argument("api_token")
@click.argument("movie_title")
@click.argument("movie_year")
def search(api_token, movie_title, movie_year):
    """Does a search for a movie by title and release year."""
    log = logging.getLogger()
    themoviedb = TheMovieDB(api_token)
    movie_match = themoviedb.search_movie(movie_title, movie_year)
    if movie_match:
        print(movie_match)
        print(movie_match.get_credits())
