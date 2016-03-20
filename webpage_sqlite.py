#!/usr/bin/env python

import fresh_tomatoes
import movie

movies = movie.get_movies()

fresh_tomatoes.open_movies_page(movies)
