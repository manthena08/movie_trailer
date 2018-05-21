class Movie:
    """ Movie is used to pass in the single movie information.
    Args:
        title: The title of the movie.
        imageUrl: The image url of the movie.
        videoUrl: The video url of the movie.
    """

    def __init__(self, title, imageUrl, videoUrl):
        self.title = title
        self.trailer_youtube_url = videoUrl
        self.poster_image_url = imageUrl
