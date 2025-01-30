
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
        print(f"Файл '{filename}' не найден.")
        return notes  # Возвращаем пустой список

    if not lines:
        print(f"Файл '{filename}' пуст.")
        return notes  # Возвращаем пустой список

    current_note = {}
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

    # Добавляем последнюю заметку, если она есть
    if current_note:
        notes.append(current_note)

    return notes

# Пример использования функции
filename = "notes.txt"
loaded_notes = load_notes_from_file(filename)
print(loaded_notes)