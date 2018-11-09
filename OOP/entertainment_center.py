import media

toy_stoty = media.Movie('Toy Story',
                        'A story of a boy and a boy his toys that come to life',
                        'https://uauposters.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/2/227020140608-uau-posters-filmes-infantis-animacao-toy-story-toy-story--1.jpg',
                        'https://www.youtube.com/watch?v=K53bxqOuThQ&ab_channel=newmoviebrasil')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://i0.wp.com/www.cinemadebuteco.com.br/wp-content/uploads/2016/06/poster-Avatar.jpg?fit=562%2C796&ssl=1',
                     'https://www.youtube.com/watch?v=2MIvbG5u1l0&ab_channel=RTP')

print(toy_stoty.storyline)
print(avatar.storyline)
