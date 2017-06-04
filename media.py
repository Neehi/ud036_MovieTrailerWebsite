import webbrowser


# Representation of a movie object.
class Movie:
    """
    A class for storing and retrieving information about a movie.

    Attributes:
        title:                  Title of the movie.
        storyline:              The movie's storyline / description.
        poster_image_url:       URL of the movie's trailer poster.
        trailer_youtube.url:    URL of the movie's official trailer.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
