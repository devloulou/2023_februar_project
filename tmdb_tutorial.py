import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

search = tmdb.Search()

response = search.movie(query='Alien')['results'][0]

print(response)
exit()

movie = tmdb.Movies(348)

for item in movie.credits()['cast']:
    if item['cast_id'] == 89:
        print(item)

# képet kiírni

#https://image.tmdb.org/t/p/original/AmR3JG1VQVxU8TfAvljUhfSFUOx.jpg

from urllib.request import urlopen

image = urlopen("https://image.tmdb.org/t/p/original/AmR3JG1VQVxU8TfAvljUhfSFUOx.jpg").read()


with open('test.jpg', "wb") as poster:
    poster.write(image)