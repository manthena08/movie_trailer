import fresh_tomatoes
import movie

avatar = movie.Movie('Avatar', './images/avatar.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')
thor = movie.Movie('Thor Ragnarok', './images/Thor_Ragnarok_poster.jpg',
                   'https://www.youtube.com/watch?v=v7MGUNV8MxU&t=26s')
black_panther = movie.Movie('Black Panther',
                            './images/Black_Panther_film_poster.jpg',
                            'https://www.youtube.com/watch?v=dxWvtMOGAhw')

movies_list = [avatar, thor, black_panther]
fresh_tomatoes.open_movies_page(movies_list)
