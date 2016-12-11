import webbrowser


class Video():
        # Define documentation
        """ This class provides a way to store video related documentation """

        def __init__(
                self, title, duration):
            self.title = movie_title
            self.duration = duration


class Movie(Video):
    # Define documentation
    """ This class provides a way to store movie related documentation """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(
            self, movie_title, movie_duration, movie_stotyline,
            movie_poster_image_url, movie_trailer_youtube_url):

        Video.__init__(self, movie_title, movie_duration)

        self.storyline = movie_stotyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    # Define documentation
    """ This class provides a way to store Tv Show related documentation """

    def __init__(
            self, serie_title, serie_duration, serie_season, serie_episode,
            serie_tv_station):

        Video.__init__(self, serie_title, serie_duration)

        self.serie_season = serie_season
        self.serie_episode = serie_episode
        self.serie_tv_station = serie_tv_station

    def get_local_listing(self):
