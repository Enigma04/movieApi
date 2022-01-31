def movie_serializer(movie) -> dict:
    return {
        'id': str(movie['_id']),
        'title': str(movie['title']),
        'summary': str(movie['summary']),
        'watched': bool(movie['watched'])
    }


def movies_serializer(movies) -> list:
    return [
        movie_serializer(movie) for movie in movies
    ]


def user_serializer(user) -> dict:
    return {
        'id': str(user['_id']),
        'name': str(user['name']),
        'email': str(user['email']),
        'password': str(user['password']),
    }


def users_serializer(users) -> list:
    return [
        user_serializer(user) for user in users
    ]
