# Movie Trailer Website
Source code for a Movie Trailer website as part of the Udacity Full Stack Web Developer Nanodegree program.

## Requirements
In order to launch the Movie Trailer Website you will require Python. If Python is not already installed on your system, it can be downloaded from [python.org](https://www.python.org/downloads/) and installation instructions for your particular platform can be found [here](https://wiki.python.org/moin/BeginnersGuide/Download).

## Getting Started
The source for the website can be found [here](https://github.com/Neehi/ud036_MovieTrailerWebsite/) on github.

### Clone
The simplest way to install the Movie Trailer website is using git to clone the repository.
```
$ git clone git@github.com:Neehi/ud036_MovieTrailerWebsite.git
```
This will install the website to a folder called ud036_MovieTrailerWebsite where the command was run from.

If you want to install the repository elsewhere, or give it a different name, then add this parameter at the end of the command.
```
$ git clone git@github.com:Neehi/ud036_MovieTrailerWebsite.git /path/to/repo
```

### Download
The alternative method to install the website is to download it directly from [here](https://github.com/Neehi/ud036_MovieTrailerWebsite/archive/master.zip).

*Please note that instructions on how to download files is beyond the scope of this guide, so please consult your operating system documentation for full instructions on how to download and unzip files.*

## How to Launch the Website
In order to launch the Movie Trailer website, simply change to the folder the website was installed to and launch it using the Python interpreter.
```
$ cd /path/to/repo
$ python entertainment_center.py
```

## Customising the Website
If you wish to customise the movies displayed on the website, then this can be done by editing the list of movies found in entertainment_center.py. As can be seen in the box below, each entry requires a title, a storyline, the URL for movie's poster image and a URL for the movie's offical trailer.
```
    ...
    media.Movie(
        "Ferris Bueller's Day Off",
        "A high school wise guy is determined to have a day off from school, despite what the prinicipal thinks of that.",
        "https://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg",
        "https://www.youtube.com/watch?v=R-P6p86px6U"
    ),
    ...
```

If instead you wish to edit the layout or markup directly, then this can be located in fresh_tomatoes.py.

Once any changes have been made, simply run the program once more using Python to see the changes take effect.

*Please note that instructions on the Python programming language or HTML/CSS is beyond the scope of this guide.*
