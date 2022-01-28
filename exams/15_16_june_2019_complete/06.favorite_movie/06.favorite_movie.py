

movie_limit = 0
total_score = 0
movie = ""

while movie_limit != 7:

    movie_title = input()


    score = 0
    if movie_title == "STOP":
        print(f"The best movie for you is {movie} with {total_score} ASCII sum.")
        break

    for i in movie_title:
        if i.isupper():
            score += ord(i) - len(movie_title)

        elif i.islower():
            score += ord(i) - len(movie_title) * 2

        else:
            score += ord(i)

    movie_limit += 1

    if score > total_score:
        total_score = score
        movie = movie_title


if movie_limit > 6:
    print(f"The limit is reached.\n"
          f"The best movie for you is {movie} with {total_score} ASCII sum.")






