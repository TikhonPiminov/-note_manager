def save_notes_to_file(notes, filename):
    """
    Сохраняет список заметок в текстовый файл в заданном формате.

    :param notes: Список словарей, где каждый словарь представляет одну заметку.
    :param filename: Имя файла, в который будут сохранены заметки.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for note in notes:
            # Формируем строку для каждой заметки в нужном формате
            formatted_note = (
                f"Имя пользователя: {note.get('username', '')}\n"
                f"Заголовок: {note.get('title', '')}\n"
                f"Описание: {note.get('content', '')}\n"
                f"Статус: {note.get('status', '')}\n"
                f"Дата создания: {note.get('created_date', '')}\n"
                f"Дедлайн: {note.get('issue_date', '')}\n"
                "---\n"
            )
            # Записываем отформатированную строку в файл
            file.write(formatted_note)


# Пример использования функции
notes = [
    {
        "username": "Иван",
        "title": "Сделать покупки",
        "content": "Купить продукты на неделю.",
        "status": "В процессе",
        "created_date": "2023-10-01",
        "issue_date": "2023-10-05"
    },
    {
        "username": "Мария",
        "title": "Позвонить бабушке",
        "content": "Не забыть позвонить сегодня вечером.",
        "status": "Выполнено",
        "created_date": "2023-10-02",
        "issue_date": "2023-10-02"
    }
]

filename = "notes.txt"
save_notes_to_file(notes, filename)