
def display_notes(notes):
    if not notes:
        print("У вас нет сохранённых заметок.")
        return

    print("Список заметок:")
    print("------------------------------")

    for i, note in enumerate(notes, start=1):
        print(f"Заметка №{i}:")
        print(f"Имя пользователя: {note.get('username', 'Не указано')}")
        print(f"Заголовок: {note.get('title', 'Не указано')}")
        print(f"Описание: {note.get('description', 'Не указано')}")
        print(f"Статус: {note.get('status', 'Не указано')}")
        print(f"Дата создания: {note.get('created_date', 'Не указано')}")
        print(f"Дедлайн: {note.get('deadline', 'Не указано')}")
        print("------------------------------")


if __name__ == "__main__":
    # Тестовый список заметок
    test_notes = [
        {
            "username": "Алексей",
            "title": "Список покупок",
            "description": "Купить продукты на неделю",
            "status": "новая",
            "created_date": "27-11-2024",
            "deadline": "30-11-2024"
        },
        {
            "username": "Мария",
            "title": "Учеба",
            "description": "Подготовиться к экзамену",
            "status": "в процессе",
            "created_date": "25-11-2024",
            "deadline": "01-12-2024"
        }
    ]

    # Вызов функции с тестовыми данными
    display_notes(test_notes)

    # Вызов функции с пустым списком
    display_notes([])