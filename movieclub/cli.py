import logging
import click
from movieclub.themoviedb import TheMovieDB
import csv

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
        click.secho(movie_match)
    else:
        click.secho("No match.", fg="red")

@cli.command()
@click.argument("api_token")
@click.argument("csv_file")
def analyse(api_token, csv_file):
    """Does a search for a movie by title and release year."""
    log = logging.getLogger()
    themoviedb = TheMovieDB(api_token)

    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            movie_match = themoviedb.search_movie(row[0], row[1])
            if movie_match:
                click.secho(movie_match._unique_name)
            else:
                click.secho(f"No match for '{row[0]} ({row[1]})'", fg="red")
