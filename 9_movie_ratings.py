movie_ratings = {'Saltburn': 8, 'Fantastic Mr. Fox': 10, 'Kung Fu Panda': 7, 'La La Land': 9, 'Wonka': 6}
movie = input('Type Movie Title: ')
print()

def recommend_movie(movie_ratings,movie):
    if movie in movie_ratings:
        for key in movie_ratings:
            if movie == key and movie_ratings[key] >= 8:
                print('Highly Recommended Movie!')
            elif movie == key and movie_ratings[key] <= 7:
                print('Movie Not Recommended')
    else:
        print('Movie Not Rated')
    print()
    print('Movies I Recommend:')
    for key in movie_ratings:
        if movie_ratings[key] >= 8:
            print(key)
    print()
            
recommend_movie(movie_ratings,movie)
