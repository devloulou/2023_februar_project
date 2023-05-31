import tmdbsimple as tmdb

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

search = tmdb.Search()

response = search.movie(query='Prey')['results'][0]

print(response)

# if not response:
#     print(10)

# movie = tmdb.Movies(348)

# for item in movie.credits()['cast']:
#     if item['cast_id'] == 89:
#         print(item)

# képet kiírni

#https://image.tmdb.org/t/p/original/AmR3JG1VQVxU8TfAvljUhfSFUOx.jpg



poster_path = "https://image.tmdb.org/t/p/original"




from urllib.request import urlopen
download_path = poster_path + response['poster_path']
image = urlopen(download_path).read()

with open('test.jpg', "wb") as poster:
    poster.write(image)