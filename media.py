import webbrowser


__author__ = "Nick Snape"
__credits__ = "Udacity"


# Representation of a movie object.
class Movie:
    """
    This class is for storing and retrieving information about a movie.

    Attributes:
        title (str) : Title of the movie.
        storyline (str): The movie's storyline / description.
        poster_image_url (str): URL of the movie's trailer poster.
        trailer_youtube.url (str): URL of the movie's official trailer.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        """
        Initialise an instance of a movie.

        Args:
            title (str): The title of the movie.
            storyline (str): The movie's storyline / description.
            poster_image_url (str): URL of the movie's trailer poster.
            trailer_youtube_url (str): URL of the movie's official trailer.
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open the movie's trailer in a web browser."""
        webbrowser.open(self.trailer_youtube_url)
