from datetime import datetime


def create_note():
    """
    Функция для создания новой заметки.
    Запрашивает у пользователя данные и возвращает словарь с информацией о заметке.
    """
    # Запрашиваем данные у пользователя
    username = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    content = input("Введите описание заметки: ")
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")

    # Запрашиваем дату дедлайна с проверкой формата
    while True:
        issue_date = input("Введите дату дедлайна (день-месяц-год): ")
        try:
            # Пытаемся преобразовать введённую дату в объект datetime
            datetime.strptime(issue_date, "%d-%m-%Y")
            break  # Если формат правильный, выходим из цикла
        except ValueError:
            print("Неверный формат даты! Пожалуйста, введите дату в формате 'день-месяц-год'.")

    # Автоматически добавляем текущую дату
    created_date = datetime.now().strftime("%d-%m-%Y")

    # Формируем словарь с данными заметки
    note = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    return note


# Демонстрация работы функции
if __name__ == "__main__":
    new_note = create_note()
    print("Заметка создана:", new_note)