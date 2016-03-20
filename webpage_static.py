import fresh_tomatoes


# Defines the Movie object structure
class Movie:
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_url = poster_url
        self.trailer_url = trailer_url

# List of movies to be displayed
movies = [
    Movie("The Revenant", "https://placekitten.com/220/342", "https://www.youtube.com/watch?v=LoebZZ8K5N0"),
    Movie("Steve Jobs",   "https://placekitten.com/220/342", "https://www.youtube.com/watch?v=ufMgQNCXy_M"),
    Movie("Toy Story 4", "https://placekitten.com/220/342", "https://www.youtube.com/watch?v=QW0sjQFpXTU")
]

# Generates and opens html gallery
fresh_tomatoes.open_movies_page(movies)
