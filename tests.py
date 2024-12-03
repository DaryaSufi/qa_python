import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_name_of_book_more_than_0_simbols(self):
        collector = BooksCollector()
        collector.add_new_book('Дом в котором')
        collector.get_books_genre()
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_one_book_twise_false(self):
        collector = BooksCollector()
        collector.add_new_book('Дом в котором')
        collector.add_new_book('Дом в котором')
        assert collector.get_books_genre() == {'Дом в котором': ''}

    def test_set_book_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        assert collector.get_book_genre('Сердце Пармы') == 'Фантастика'

    def test_get_book_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        assert collector.get_book_genre('Сердце Пармы') == 'Фантастика'

    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        collector.get_books_with_specific_genre('Фантастика')
        assert 'Сердце Пармы' in collector.get_books_with_specific_genre('Фантастика')

    def test_get_books_with_specific_genre_false(self):
        collector = BooksCollector()
        collector.add_new_book('Влипсики')
        collector.set_book_genre('Влипсики', 'Фэнтези')
        collector.get_books_with_specific_genre('Фэнтези')
        assert len(collector.get_books_with_specific_genre('Фэнтези')) == 0

    def test_get_books_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        assert collector.get_books_genre() == {'Сердце Пармы': 'Фантастика'}

    def test_get_books_for_children_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        collector.add_new_book('Моана')
        collector.set_book_genre('Моана', 'Мультфильмы')
        collector.get_books_for_children()
        assert collector.get_books_for_children() == ['Сердце Пармы', 'Моана']

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.add_book_in_favorites('Сердце Пармы')
        assert collector.get_list_of_favorites_books() == ['Сердце Пармы']

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_book_in_favorites('Кошмар на улице Вязов')
        collector.delete_book_from_favorites('Кошмар на улице Вязов')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.add_book_in_favorites('Сердце Пармы')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_book_in_favorites('Кошмар на улице Вязов')
        collector.get_list_of_favorites_books()
        assert collector.get_list_of_favorites_books() == ['Сердце Пармы', 'Кошмар на улице Вязов']

    @pytest.fixture
    def books_collector(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        collector.add_book_in_favorites('Сердце Пармы')

        collector.add_new_book('Кошмар на улице Вязов')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        collector.add_book_in_favorites('Кошмар на улице Вязов')

        return collector

    @pytest.mark.parametrize("name", ['Сердце Пармы', 'Кошмар на улице Вязов'])
    def test_get_list_of_favorites_books_true(books_collector, name):
        collector = books_collector
        collector.get_list_of_favorites_books()
        assert collector.get_list_of_favorites_books() == [name]

