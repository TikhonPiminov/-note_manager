def search_notes(notes, keyword=None, status=None):
    # Фильтрация заметок по ключевому слову и статусу
    filtered_notes = []
    for note in notes:
        # Проверка по ключевому слову, если оно задано
        keyword_match = keyword is None or any(
            keyword.lower() in note[field].lower() for field in ['title', 'content', 'username'])
        # Проверка по статусу, если он задан
        status_match = status is None or note['status'].lower() == status.lower()
        # Если оба условия выполнены, добавляем заметку в результат
        if keyword_match and status_match:
            filtered_notes.append(note)

    # Вывод результата
    if not filtered_notes:
        print("Заметки, соответствующие запросу, не найдены.")
    else:
        print("Найдены заметки:")
        for i, note in enumerate(filtered_notes, start=1):
            print(f"Заметка №{i}:")
            print(f"Имя пользователя: {note['username']}")
            print(f"Заголовок: {note['title']}")
            print(f"Описание: {note['content']}")
            print(f"Статус: {note['status']}")
            print()


# Пример использования
notes = [
    {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая',
     'created_date': '27-11-2024', 'issue_date': '30-11-2024'},
    {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе',
     'created_date': '25-11-2024', 'issue_date': '01-12-2024'},
    {'username': 'Иван', 'title': 'План работы', 'content': 'Завершить проект', 'status': 'выполнено',
     'created_date': '20-11-2024', 'issue_date': '26-11-2024'}
]

# Примеры вызовов функции
search_notes(notes, keyword='покупок')
search_notes(notes, status='в процессе')
search_notes(notes, keyword='работы', status='выполнено')