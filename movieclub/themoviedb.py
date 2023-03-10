from movieclub.framework.rest_api import RestAPI
from movieclub.obj.movie import Movie
from movieclub.helpers import similar
from movieclub.api.user_access import UserAccess


class TheMovieDB(RestAPI):
    def __init__(self, config):
        """Used to interact with TheMovieDB Rest API"""
        super().__init__("https://api.themoviedb.org/3/", config)
        self.user = UserAccess(config)

    def search_movie(self, title, year):
        """Search for a movie by title and release year."""
        movie_match = None
        params = {
            "query": title,
            "year": year,
            "page": 1,
            "include_adult": False,
        }
        resp = self.get("search/movie", params)
        for match in resp.get("results", []):
            # match both the movie title and expected release year
            if similar(match.get("title"), title) >= 0.95 and \
                    match.get("release_date").startswith(year):
                movie_match = self.get_movie(match["id"])
                break
        return movie_match

    def get_movie(self, id):
        """Gets the movie data by id (TMDB Movie ID)."""
        return Movie(self, self.get(f"movie/{id}"))

    def get_similar_movies(self, id):
        """Returns a list of moves similiar to the selected movie."""
        return [Movie(self, data) for data in self.get(f"movie/{id}/similar").get("results", [])]
