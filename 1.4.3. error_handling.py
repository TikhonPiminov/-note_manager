
def save_notes_to_file(notes, filename):
    """
    Сохраняет список заметок в текстовый файл в заданном формате.

    :param notes: Список словарей, где каждый словарь представляет одну заметку.
    :param filename: Имя файла, в который будут сохранены заметки.
    """
    try:
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
        print(f"Заметки успешно сохранены в файл '{filename}'.")
    except IOError as e:
        print(f"Ошибка при записи в файл '{filename}': {e}")

def load_notes_from_file(filename):
    """
    Загружает заметки из текстового файла и возвращает их в виде списка словарей.

    :param filename: Имя файла, из которого будут загружены заметки.
    :return: Список словарей с заметками или пустой список, если файл отсутствует или пуст.
    """
    notes = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Создан новый файл.")
        # Создаем новый файл
        with open(filename, 'w', encoding='utf-8') as new_file:
            pass  # Просто создаем файл, ничего не записывая
        return notes  # Возвращаем пустой список
    except IOError as e:
        print(f"Ошибка при чтении файла '{filename}': {e}")
        return notes  # Возвращаем пустой список

    if not lines:
        print(f"Файл '{filename}' пуст.")
        return notes  # Возвращаем пустой список

    current_note = {}
    malformed_note = False
    for line in lines:
        line = line.strip()
        if line.startswith("Имя пользователя:"):
            if current_note:
                notes.append(current_note)
            current_note = {'username': line.replace("Имя пользователя: ", "")}
        elif line.startswith("Заголовок:"):
            current_note['title'] = line.replace("Заголовок: ", "")
        elif line.startswith("Описание:"):
            current_note['content'] = line.replace("Описание: ", "")
        elif line.startswith("Статус:"):
            current_note['status'] = line.replace("Статус: ", "")
        elif line.startswith("Дата создания:"):
            current_note['created_date'] = line.replace("Дата создания: ", "")
        elif line.startswith("Дедлайн:"):
            current_note['issue_date'] = line.replace("Дедлайн: ", "")
        elif line == "---":
            if current_note:
                notes.append(current_note)
                current_note = {}
        else:
            print(f"Ошибка при чтении файла '{filename}'. Проверьте его содержимое.")
            malformed_note = True
            break

    if current_note and not malformed_note:
        notes.append(current_note)

    if malformed_note:
        return []  # Возвращаем пустой список, если данные некорректны

    print(f"Заметки успешно загружены из файла '{filename}'.")
    return notes

# Пример использования функций
if __name__ == "__main__":
    # Пример заметок для сохранения
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

    # Сохранение заметок в файл
    save_notes_to_file(notes, filename)

    # Загрузка заметок из файла
    loaded_notes = load_notes_from_file(filename)
    print("Загруженные заметки:")
    print(loaded_notes)