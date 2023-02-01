import pytest

from service.movie import MovieService


class TestMovieService:

    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Movie 1"

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert movies is not None
        assert len(movies) > 0
        assert len(movies) == 3

    def test_create(self):
        movie_dict = {
            'id': 1,
            'title': 'Movie 1',
            'description': 'Description',
            'year': 2023,
            'rating': 5.0,
            'genre_id': 1,
            'director_id': 1,
            'trailer': 'Trailer'
        }

        movie = self.movie_service.create(movie_dict)
        assert movie.id is not None
        assert movie.title == 'Movie 1'

    def test_delete(self):
        assert self.movie_service.delete(1) is None

    def test_update(self):
        movie_dict = {
            'title': 'Movie 1',
            'description': 'Description',
            'year': 2023,
            'rating': 5.0,
            'genre_id': 1,
            'director_id': 1,
            'trailer': 'Trailer'
        }
        assert self.movie_service.update(movie_dict) is not None

