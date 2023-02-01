import pytest

from service.genre import GenreService


class TestGenreService:

    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):

        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):

        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None
        assert genre.name == 'Genre 1'

    def test_get_all(self):

        genres = self.genre_service.get_all()

        assert genres is not None
        assert len(genres) > 0
        assert len(genres) == 3

    def test_create(self):

        gen_dict = {
            'id': 1,
            'name': 'Genre 1'
        }

        genre = self.genre_service.create(gen_dict)

        assert genre.id is not None
        assert genre.name == 'Genre 1'

    def test_delete(self):

        assert self.genre_service.delete(1) is None

    def test_update(self):

        gen_dict = {
            'id': 1,
            'name': 'Genre 1'
        }

        assert self.genre_service.update(gen_dict) is not None

