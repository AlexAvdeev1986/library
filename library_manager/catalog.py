from library_manager.utils.data_validation import validate_book_data

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title: str, author: str, genre: str) -> bool:
        """Добавляет книгу после валидации данных"""
        book_data = {'title': title, 'author': author, 'genre': genre}
        if validate_book_data(book_data):
            self.books.append(book_data)
            return True
        return False
    
    def remove_book_by_title(self, title: str) -> bool:
        """Удаляет книги по названию"""
        initial_count = len(self.books)
        self.books = [book for book in self.books if book['title'] != title]
        return len(self.books) < initial_count
    
    def search_books(self, title: str = None, author: str = None, genre: str = None) -> list:
        """Ищет книги по критериям (логическое И)"""
        results = []
        for book in self.books:
            match = True
            if title and book['title'] != title:
                match = False
            if author and book['author'] != author:
                match = False
            if genre and book['genre'] != genre:
                match = False
            if match:
                results.append(book)
        return results
    
    def get_all_books(self) -> list:
        """Возвращает копию списка всех книг"""
        return self.books.copy()
    