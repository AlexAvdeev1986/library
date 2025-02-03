# main.py
from library_manager import Library, generate_report

def main():
    # Создаем экземпляр библиотеки
    lib = Library()
    
    # Добавляем книги
    lib.add_book("1984", "Джордж Оруэлл", "Антиутопия")
    lib.add_book("Мастер и Маргарита", "Михаил Булгаков", "Роман")
    
    # Генерируем отчет
    print("=== Полный отчет ===")
    print(generate_report(lib))
    
    # Ищем книги
    print("\n=== Результаты поиска ===")
    results = lib.search_books(author="Джордж Оруэлл")
    for book in results:
        print(f"Найдено: {book['title']}")
    
    # Удаляем книгу
    lib.remove_book_by_title("1984")
    print("\n=== После удаления ===")
    print(generate_report(lib))

if __name__ == "__main__":
    main()
    