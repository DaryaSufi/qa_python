import pytest

from main import BooksCollector

class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize('name',['Д','До','Дом в котором'])
    def test_add_new_book_add_name_of_book_more_than_0_simbols(self,name):
        collector = BooksCollector()
        assert collector.add_new_book(name)
    def test_add_new_book_add_one_book_twise_false(self):
        collector = BooksCollector()
        collector.add_new_book('Дом в котором')
        collector.add_new_book('Дом в котором')
        assert len(self.books_genre)==1
    def test_set_book_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        assert self.books_genre['Сердце Пармы'] == {'Сердце Пармы':'Фантастика'}
    def test_get_book_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        assert self.collector.get_book_genre('Сердце Пармы')=='Фантастика'
    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        collector.get_books_with_specific_genre('Фантастика')
        assert 'Сердце Пармы' in self.books_with_specific_genre
    def test_get_books_with_specific_genre_false(self):
        collector = BooksCollector()
        collector.add_new_book('Влипсики')
        collector.set_book_genre('Влипсики', 'Фэнтези')
        collector.get_books_with_specific_genre('Фэнтези')
        assert len(self.books_with_specific_genre)==0
    def test_get_books_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.set_book_genre('Сердце Пармы', 'Фантастика')
        assert self.books_genre == {'Сердце Пармы':'Фантастика'}
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
        assert self.books_for_children == ['Сердце Пармы', 'Моана']
    def test_add_book_in_favorites_true(self, name):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.add_book_in_favorites('Сердце Пармы')
        assert self.favorites == ['Сердце Пармы']
    def test_delete_book_from_favorites_true(self,name):
        collector = BooksCollector()
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_book_in_favorites('Кошмар на улице Вязов')
        collector.delete_book_from_favorites('Кошмар на улице Вязов')
        assert self.favorites == []
    def test_get_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Сердце Пармы')
        collector.add_book_in_favorites('Сердце Пармы')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_book_in_favorites('Кошмар на улице Вязов')
        collector.get_list_of_favorites_books()
        assert self.collector.get_list_of_favorites_books==self.favorites























