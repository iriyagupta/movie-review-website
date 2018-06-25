import webbrowser
import urllib


class Video():
    """This is the documentation of trailers"""
    def __init__(self, movie_title,duration_time):
        self.title= movie_title
        self.duration = duration_time
    
class Media(Video):
    """This is the documentation of trailers"""
    ratings= ["P","3 stars"]
    def __init__(self ,movie_title ,duration_time, movie_storyline , poster_image , trailer_youtube):
        Video.__init__(self, movie_title,duration_time)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def trailers(self):
        webbrowser.open(self.trailer_youtube_url)


class TV(Video):
    """This is the documentation of trailers"""
    ratings= ["P","3 stars"]
    def __init__(self ,movie_title ,duration_time, movie_storyline , poster_image , trailer_youtube):
        Video.__init__(self, movie_title,duration_time)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def trailers(self):
        webbrowser.open(self.trailer_youtube_url)
