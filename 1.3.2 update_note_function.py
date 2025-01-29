
from datetime import datetime

def validate_date(date_str):
    """
    Проверяет корректность формата даты (день-месяц-год).
    Возвращает True, если формат правильный, иначе False.
    """
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def update_note(note):
    """
    Функция для обновления заметки.
    Принимает заметку (словарь) и возвращает обновлённый словарь.
    """
    # Показываем текущие данные заметки
    print("Текущие данные заметки:")
    print(note)

    # Список доступных полей для обновления
    fields = ["username", "title", "content", "status", "issue_date"]

    # Запрашиваем у пользователя поле для обновления
    while True:
        field = input("Какие данные вы хотите обновить? (username, title, content, status, issue_date): ").strip().lower()
        if field in fields:
            break  # Если поле корректное, выходим из цикла
        else:
            print("Ошибка: некорректное имя поля. Пожалуйста, выберите одно из: username, title, content, status, issue_date.")

    # Запрашиваем новое значение для выбранного поля
    new_value = input(f"Введите новое значение для {field}: ").strip()

    # Если обновляется поле issue_date, проверяем формат даты
    if field == "issue_date":
        while not validate_date(new_value):
            print("Неверный формат даты! Пожалуйста, введите дату в формате 'день-месяц-год'.")
            new_value = input(f"Введите новое значение для {field}: ").strip()

    # Обновляем выбранное поле
    note[field] = new_value

    # Возвращаем обновлённую заметку
    print("Заметка обновлена:")
    return note

# Демонстрация работы функции
if __name__ == "__main__":
    # Пример заметки для тестирования
    example_note = {
        "username": "Алексей",
        "title": "Список покупок",
        "content": "Купить продукты на неделю",
        "status": "новая",
        "created_date": "27-11-2024",
        "issue_date": "30-11-2024"
    }

    # Вызываем функцию и выводим результат
    updated_note = update_note(example_note)
    print(updated_note)