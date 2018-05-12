class Movie:
    # Movie class takes in title, imageUrl, Trailer url.
    def __init__(self, title, imageUrl, videoUrl):
        self.title = title
        self.trailer_youtube_url = videoUrl
        self.poster_image_url = imageUrl
