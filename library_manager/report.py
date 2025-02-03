from library_manager.utils.formatting import format_book_data

def generate_report(library) -> str:
    """Генерирует текстовый отчет о книгах"""
    books = library.get_all_books()
    if not books:
        return "В библиотеке нет книг"
    return "\n".join([format_book_data(book) for book in books])
