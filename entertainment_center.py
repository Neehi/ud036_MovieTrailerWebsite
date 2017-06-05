import fresh_tomatoes
import media


__author__ = "Nick Snape"
__credits__ = "Udacity"


# Create the movie list ready for use by fresh_tomatoes.
movies = [
    media.Movie(
        "Ferris Bueller's Day Off",
        "A high school wise guy is determined to have a day off from school, "
        "despite what the prinicipal thinks of that.",
        "https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg",
        "https://www.youtube.com/watch?v=R-P6p86px6U"
    ),
    media.Movie(
        "The Blues Brothers",
        "Jake Blues, just out from prison, puts together his old band to save "
        "the Catholic home where he and brother Elwood were raised.",
        "https://upload.wikimedia.org/wikipedia/en/f/f5/BluesBrothers.jpg",
        "https://www.youtube.com/watch?v=2HCR4c1zPyk"
    ),
    media.Movie(
        "The Rocky Horror Picture Show",
        "A newly engaged couple have a breakdown in an isolated area and must "
        "pay a call to the bizarre residence of Dr. Frank-N-Furter.",
        "https://upload.wikimedia.org/wikipedia/en/c/c2/Original_Rocky_Horror_Picture_Show_poster.jpg",
        "https://www.youtube.com/watch?v=863kmtYD1zM"
    ),
    media.Movie(
        "The Matrix",
        "A computer hacker learns from mysterious rebels about the true nature "
        "of his reality and his role in the war against its controllers.",
        "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
        "https://www.youtube.com/watch?v=vKQi3bBA1y8"
    ),
    media.Movie(
        "Blade Runner",
        "A blade runner must pursue and try to terminate four replicants who "
        "stole a ship in space and have returned to Earth to find their creator.",
        "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
        "https://www.youtube.com/watch?v=eogpIG53Cis"
    ),
    media.Movie(
        "Pulp Fiction",
        "The lives of two mob hit men, a boxer, a gangster's wife, and a pair "
        "of diner bandits intertwine in four tales of violence and redemption.",
        "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
        "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
    )
]

# Pass the list of movies to fresh_tomatoes, so it can build
# the web page and attempt to open it in a new browser tab.
fresh_tomatoes.open_movies_page(movies)
