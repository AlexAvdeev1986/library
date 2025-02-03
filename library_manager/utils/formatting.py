def format_book_data(data: dict) -> str:
    """Форматирует данные книги для вывода"""
    return f"Название: {data['title']}, Автор: {data['author']}, Жанр: {data['genre']}"
