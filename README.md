#Movie Trailer Website

A simple static generator to display a gallery of movie titles, posters, and trailers.

### Contributing

Contributions are welcome! Just fork this repo, make your own changes, and submit it as a pull request.

##Static Site

###Usage:

```
./webpage_static.py
```

If the above does not run, you may need to make it writable:

```
chmod +x webpage_static.py
```

---

##SQLite Site

###Usage:

```
./webpage_sqlite.py
```

To add a new movie to the database run the following:

```
./add_movie_to_database.py --title "Title Here" --poster "URL To Poster Image" --trailer "URL To Youtube Trailer"
```

## To Do
- Allow a JSON or YAML file to be used as input rather than just the static array