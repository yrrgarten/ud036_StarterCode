# -*- coding: utf-8 -*-

""" Media Center build script.

This module builds a HTML file with a given number of favorite movies. The HTML
base skeleton comes from fresh_tomatoes module, the class movie from the movie
module.

Usage:
    The module should directly be called, e.g.:
        $ python media_center.py

    The output HTML will be saved in the same folder.
"""

import movie
import fresh_tomatoes

# Initialize 6 movie objects with favorite movies
pulp = movie.Movie("Pulp Fiction",
                   "So this is where the Travolta Meme is coming from.",
                   "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                   "https://www.youtube.com/watch?v=s7EdQ4FqbhY",
                   1994)
inst = movie.Movie("Interstellar",
                   "Matthew McConnaley tring to grt back",
                   "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                   "https://www.youtube.com/watch?v=FByEFOAQeU0",
                   2014)
bldr = movie.Movie("Blade Runner",
                   "The original.",
                   "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                   "https://www.youtube.com/watch?v=eogpIG53Cis",
                   1982)
btfm = movie.Movie("A Beautiful Mind",
                   "A tribute to John Nash.",
                   "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",
                   "https://www.youtube.com/watch?v=aS_d0Ayjw4o",
                   2001)
fezb = movie.Movie("Die Feuerzangenbowle",
                   "Pännaler in der Schule.",
                   "https://upload.wikimedia.org/wikipedia/en/9/91/FZB2002cover.jpg",
                   "https://www.youtube.com/watch?v=7NWfFVCcZdk",
                   1944)
incp = movie.Movie("Inception",
                   "Spinning round and round.",
                   "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                   "https://www.youtube.com/watch?v=d3A3-zSOBT4",
                   2010)

movies = [pulp, inst, bldr, btfm, fezb, incp]
# render the output HTML file with the movies from the movies list
fresh_tomatoes.open_movies_page(movies)
