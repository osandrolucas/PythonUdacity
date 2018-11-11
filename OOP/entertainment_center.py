import media

from OOP import page_movies

toy_stoty = media.Movie('Toy Story',
                        'A story of a boy and a boy his toys that come to life',
                        'https://uauposters.com.br/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/2/227020140608-uau-posters-filmes-infantis-animacao-toy-story-toy-story--1.jpg',
                        'https://www.youtube.com/watch?v=K53bxqOuThQ&ab_channel=newmoviebrasil')

avatar = media.Movie('Avatar',
                     'A marine on an alien planet',
                     'https://i0.wp.com/www.cinemadebuteco.com.br/wp-content/uploads/2016/06/poster-Avatar.jpg?fit=562%2C796&ssl=1',
                     'https://www.youtube.com/watch?v=2MIvbG5u1l0&ab_channel=RTP')
now_you_see_me = media.Movie('Now You See Mee 2',
                            'One year after outwitting the FBI and winning the public’s adulation with their Robin Hood-style magic spectacles, the illusionists resurface for a comeback performance in hopes of exposing the unethical practices of a tech magnate.',
                            'http://t0.gstatic.com/images?q=tbn:ANd9GcTHHqZfKziQgmf70iPZLOtQTlWhpAWw6FwVFsdaUJsYiAjmkAFC',
                            'https://www.youtube.com/watch?v=3QFa2h0e22s&ab_channel=Cinemaginando')

school_of_rock = media.Movie('School of Rock',
                            'Using rock music to listen',
                            'https://static1.squarespace.com/static/560c269ae4b0c2b90045b5a4/t/5786b7546a49637b8a1793a0/1468446553014/',
                            'https://www.youtube.com/watch?v=XCwy6lW5Ixc&ab_channel=InvaderZimJr')

ratatouille = media.Movie('Ratatouille',
                            'A rat is a chef in Paris',
                            'https://i.pinimg.com/originals/01/68/df/0168dfb58adb50846ab2e670f2635c9d.jpg',
                            'https://www.youtube.com/watch?v=I9K-ehX4RqA&ab_channel=CineKidsTrailers')

midnight_in_paris = media.Movie('Midnithg in Paris',
                            'Going back in time to meet authors',
                            'https://clubedecinemapetropolis.files.wordpress.com/2015/03/midnight-in-paris-poster-artwork-kathy-bates-adrien-brody-carla-bruni.jpg?resize=333%2C500',
                            'https://www.youtube.com/watch?v=T8J1ocoMPtI&ab_channel=V%C3%ADtorOliveira')

deadpool2 = media.Movie('Deadpool 2',
                       'After successfully working as the mercenary Deadpool for two years, Wade Wilson fails to kill one of his targets on his anniversary with Vanessa, his girlfriend. That night, after the pair decide to start a family together, the target tracks Wilson down and kills Vanessa. Wilson kills the man in revenge. He blames himself for her death and attempts to commit suicide six weeks later by blowing himself up. Wilson has a vision of Vanessa in the afterlife, but the pieces of his body remain alive and are put back together by Colossus. Wilson is left with only a Skee-Ball token, an anniversary gift, as a final memento of Vanessa.',
                       'http://t0.gstatic.com/images?q=tbn:ANd9GcQk4VujIOVqKQGdAk-MUHoGKTSyRHg8lzTnZsCpTuxOTle7BWP7',
                       'https://www.youtube.com/watch?v=1P9OzWX6nzE&ab_channel=FoxFilmdoBrasil')

zohan = media.Movie('Zohan',
                       'An Israeli Special Forces Soldier fakes his death so he can re-emerge in New York City as a hair stylist.',
                       'https://media1.jpc.de/image/w600/front/0/4030521715943.jpg',
                       'https://www.youtube.com/watch?v=9zNZM_ZCIrc&ab_channel=Zohan-OAgenteBomDeCorte%28LEG%29-Trailer')

te_peguei = media.Movie('Te Peguei!',
                       'A história de amigos que brincam de pega pega todo o ano.',
                       'http://t1.gstatic.com/images?q=tbn:ANd9GcQ4fUml3CHTdM_AbhRJ9lbt7HFMkikdRhesqZvIB6Wz6YSimKZe',
                       'https://www.youtube.com/watch?v=b8A12w4RqOY&ab_channel=SpaceTrailers')



movies = [deadpool2, te_peguei, zohan, now_you_see_me, toy_stoty, school_of_rock, ratatouille, midnight_in_paris, avatar]

page_movies.open_movies_page(movies)

#print('Váriaveis de classe: {}'.format(media.Movie.VARIAVEIS_DE_CLASSE))
#print('Documentation of class: {}'.format(media.Movie.__doc__))
#print('Name of class: {}'.format(media.Movie.__name__))
#print('Module of class: {}'.format(media.Movie.__module__))

#print(toy_stoty.storyline)
#print(avatar.storyline)
#avatar.show_trailer()
#now_you_see_me.show_trailer()