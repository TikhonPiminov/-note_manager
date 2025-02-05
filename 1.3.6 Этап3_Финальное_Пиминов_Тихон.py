

1. create_note_function.py

Функция create_note() запрашивает данные у пользователя для создания заметки.
Формирует словарь с полями заметки, включая автоматическую генерацию текущей даты.
Проверяет корректность формата даты дедлайна.

Пример вызова:

Введите имя пользователя: Тихон
Введите заголовок заметки: Стихи
Введите описание заметки: мороз и солнце
Введите статус заметки (новая, в процессе, выполнено): новая
Введите дату дедлайна (день-месяц-год): 18-03-2025
Заметка создана: {'username': 'Тихон ', 'title': 'Стихи', 'content': 'мороз и солнце',
                  'status': 'новая', 'created_date': '29-01-2025', 'issue_date': '18-03-2025'}

#_____________________________________________________________________________________________________________________/



2. update_note_function.py

Функция update_note(note) принимает заметку (словарь) как аргумент.
Позволяет пользователю выбрать поле для обновления.
Проверяет корректность ввода и обновляет выбранное поле.

Пример вызова:

Текущие данные заметки:
{'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}

Какие данные вы хотите обновить? (username, title, content, status, issue_date): username
Введите новое значение для username: Тихон

Заметка обновлена:
{'username': 'Тихон', 'title': 'Список покупок', 'content': 'Купить продукты на неделю',
 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}

#_____________________________________________________________________________________________________________________/


3. display_notes_function.py

Функция display_notes(notes) принимает список заметок.
Выводит каждую заметку в удобном формате.
Обрабатывает пустые списки заметок.

Пример вызова:

Список заметок:
------------------------------
Заметка №1:
Имя пользователя: Алексей
Заголовок: Список покупок
Описание: Купить продукты на неделю
Статус: новая
Дата создания: 27-11-2024
Дедлайн: 30-11-2024
------------------------------
Заметка №2:
Имя пользователя: Мария
Заголовок: Учеба
Описание: Подготовиться к экзамену
Статус: в процессе
Дата создания: 25-11-2024
Дедлайн: 01-12-2024
------------------------------
У вас нет сохранённых заметок.
#_____________________________________________________________________________________________________________________/


4. search_notes_function.py

Функция search_notes(notes, keyword=None, status=None) ищет заметки по ключевым словам или статусу.
Возвращает список найденных заметок.
Выводит сообщение, если ничего не найдено.

Пример вызова:

Найдены заметки:
Заметка №1:
Имя пользователя: Алексей
Заголовок: Список покупок
Описание: Купить продукты на неделю
Статус: новая

Найдены заметки:
Заметка №1:
Имя пользователя: Мария
Заголовок: Учеба
Описание: Подготовиться к экзамену
Статус: в процессе

Найдены заметки:
Заметка №1:
Имя пользователя: Иван
Заголовок: План работы
Описание: Завершить проект
Статус: выполнено
#_____________________________________________________________________________________________________________________/


5. menu.py

Выводит интерактивное меню для выбора действий.
Обрабатывает выбор пользователя и вызывает соответствующую функцию.
Повторяет показ меню до тех пор, пока пользователь не выберет выход.

Доступные действия:

1: Создать новую заметку (create_note()).
2: Показать все заметки (display_notes()).
3: Обновить заметку (update_note()).
4: Удалить заметку (delete_note() — опционально).
5: Найти заметки (search_notes()).
6: Выйти из программы.

Пример работы:

Меню действий:
1. Создать новую заметку
2. Показать все заметки
3. Обновить заметку
4. Удалить заметку
5. Найти заметки
6. Выйти из программы

Ваш выбор: 1
Новая заметка создана!

Меню действий:
1. Создать новую заметку
2. Показать все заметки
3. Обновить заметку
4. Удалить заметку
5. Найти заметки
6. Выйти из программы

Ваш выбор: 4
Заметка удалена!

Меню действий:
1. Создать новую заметку
2. Показать все заметки
3. Обновить заметку
4. Удалить заметку
5. Найти заметки
6. Выйти из программы

Ваш выбор: 6
Программа завершена. Спасибо за использование!
