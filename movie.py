import webbrowser


class Movie():
    """ This class holds all information of a movie.

    Args:
        movie_title (str): The title of the movie
        movie_storyline (str): A one sentence storyline o the movie
        poster_image (str): A URL of a film poster of the movie
        trailer_youtube (str): A URL of a trailer of the movie on Youtube
        release_year (int): The year of the release of the movie
    """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = release_year
