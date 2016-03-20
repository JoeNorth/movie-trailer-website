#!/usr/bin/env python

import argparse
import movie


# Describes what our files does
parser = argparse.ArgumentParser(description="Add a movie to the movies database")

# Adding arguments to the file
parser.add_argument('--title', help="Movie title", required=True)
parser.add_argument('--poster', help="URL to movie poster", required=True)
parser.add_argument('--trailer', help="URL to movie trailer", required=True)

# Parses user input and assigns them to respective variables. E.g. --title maps to args.title
args = parser.parse_args()

# Passes our arguments to the create_movie function and persists it to the database
movie.create_movie(title=args.title, poster_url=args.poster, trailer_url=args.trailer)
