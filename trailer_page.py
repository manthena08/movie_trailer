import fresh_tomatoes
import movie

avatar = movie.Movie('Avatar', './images/avatar.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')
thor = movie.Movie('Thor Ragnarok', './images/Thor_Ragnarok_poster.jpg',
                   'https://www.youtube.com/watch?v=v7MGUNV8MxU&t=26s')
black_panther = movie.Movie('Black Panther',
                            './images/Black_Panther_film_poster.jpg',
                            'https://www.youtube.com/watch?v=dxWvtMOGAhw')
wall_street = movie.Movie('The Wolf of Wall Street',
                          './images/wall_street.jpg',
                          'https://www.youtube.com/watch?v=iszwuX1AK6A')
dunkirk = movie.Movie('Dunkirk',
                      './images/dunkirk.jpeg',
                      'https://www.youtube.com/watch?v=F-eMt3SrfFU')
quiet_place = movie.Movie('A Quiet Place',
                          './images/A_Quiet_Place_film_poster.png',
                          'https://www.youtube.com/watch?v=WR7cc5t7tv8')

movies_list = [avatar, thor, black_panther, wall_street, dunkirk, quiet_place]
fresh_tomatoes.open_movies_page(movies_list)
