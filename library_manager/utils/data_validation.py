def validate_book_data(data: dict) -> bool:
    """Проверяет корректность данных книги"""
    required_fields = ['title', 'author', 'genre']
    for field in required_fields:
        if field not in data:
            return False
        if not isinstance(data[field], str):
            return False
        if not data[field].strip():
            return False
    return True
