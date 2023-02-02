import logging
import os.path
import click
import csv
import pprint
from pathlib import Path
from movieclub.themoviedb import TheMovieDB
from movieclub.helpers import create_counter
from movieclub.framework.config import Config

@click.group()
@click.version_option()
@click.option("--config-path", default="%AppData%\movieclub")
@click.pass_context
def cli(ctx, config_path):
    """movie club test"""
    config_path = Path(os.path.expandvars(config_path))
    config_file = config_path / "config.yml"
    if not config_file.exists():
        config_path.mkdir(parents=True, exist_ok=True)
        with open(config_file, "w") as file:
            file.writelines(["# movie club configuration for theMovieDB\n", "api_key:\n", "user_token:\n"])

    ctx.obj = Config(config_file)

@cli.command()
@click.argument("movie_title")
@click.argument("movie_year")
@click.pass_context
def search(ctx, movie_title, movie_year):
    """Does a search for a movie by title and release year."""
    log = logging.getLogger()
    themoviedb = TheMovieDB(ctx.obj.api_key)
    movie_match = themoviedb.search_movie(movie_title, movie_year)
    if movie_match:
        click.secho(movie_match)
    else:
        click.secho("No match.", fg="red")

@cli.command()
@click.argument("csv_file")
@click.pass_context
def analyse(ctx, csv_file):
    """Does a search for a movie by title and release year."""
    log = logging.getLogger()
    themoviedb = TheMovieDB(ctx.obj.api_key)

    all_crew = []
    all_cast = []
    all_keywords = []
    all_similiar_movies = []

    with open(csv_file) as file:
        reader = csv.reader(file)
        for row in reader:
            movie_match = themoviedb.search_movie(row[0], row[1])
            if movie_match:
                click.secho(movie_match._unique_name)
                credits = movie_match.get_credits()
                all_crew.extend([f"{c['name']} ({c['job']})" for c in credits["crew"]])
                all_cast.extend([c["name"] for c in credits["cast"]])
                keywords = movie_match.get_keywords()
                all_keywords.extend([c["name"] for c in movie_match.get_keywords()])
                all_similiar_movies.extend([m.title for m in themoviedb.get_similar_movies(movie_match.id)])
            else:
                click.secho(f"No match for '{row[0]} ({row[1]})'", fg="red")

    crew_count = create_counter(all_crew, 4)
    click.secho("crew member + job occurances:")
    click.secho(pprint.pp(crew_count, indent=3))

    cast_count = create_counter(all_cast)
    click.secho("cast member occurances:")
    click.secho(pprint.pp(cast_count, indent=3))

    keyword_count = create_counter(all_keywords, 5)
    click.secho("keyword occurances:")
    click.secho(pprint.pp(keyword_count, indent=3))

    sim_move_count = create_counter(all_similiar_movies, 8)
    click.secho("similar movies occurances:")
    click.secho(pprint.pp(sim_move_count, indent=3))