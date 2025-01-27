

Gret: 1 Этап: 2 Задание: 6

Цель финального задания:
Собрать все результаты задач этапа 2 в одном месте, чтобы продемонстрировать навыки работы с циклами, условиями,
списками и словарями. Вы должны реализовать интерактивный функционал для работы с заметками.

Цель №1  Добавление заголововков.

Решение: 1.2.1 add_titkes_loop.py

Выводит взоможный функицонал Note, ожидая ввода выбранной команды из предложенных .
После выбора команды ,,новая заметка,, пользователю предлогается заполнить форму ззаметки, пример ;

            Выберите действие;
            1 - Новая заметка;
            2 - Просмотреть все заметки;
            3 - Удалить заметку;
            4 - Выйти;

            Введите название операции: 1
            Ваш логин: Тихон
            Название заметки : Ситихи
            Описание заметки: Мороз и солнце
            Дэдлан заметки (дд-мм-гггг): 17-09-2025

Цель №2 Проверка и обновление статуса заметки
Решение: 1.2.2 update_status.py

После запонения формы заметки , прелогается выбрать статус заметки .
Статус заметки выберается из предложенных, пример ;

            Статус заметки:
            1 - В работе.
            2 - Отложенно.
            3 - Завершенно.
            4 - Выход
            Введите сатут заметки: 1
            Статус: в работе.

Цель №3  Обработка дедлайнов

Решение: 1.2.3 check_deadline.py

После создания пользователем заметки , и ввода в форму заметки даты дэдланай ,
пользователю выводится количество дней до дэдлана с датой создания заметки и датой дэдлайна

            Дата создания заметки : 27-01-2025
            Дата дэдлана (дд-мм-гггг); 19-03-2025
            До дэдлайна осталось 51 дней.

Цель №4 Работа с несколькими заметками

Решение: 1.2.4 ultiple_notes.py

После создания заметки пользователь может посмотреть имеющиеся заметки ,
введя команду для выполнения нужной функции , пример;

            Выберите действие;
            1 - Новая заметка;
            2 - Просмотреть все заметки;
            3 - Удалить заметку;
            4 - Выйти;

            Введите название операции: 1
            Ваш логин: Тихон
            Название заметки : Ситихи
            Описание заметки: Мороз и солнце
            Дэдлан заметки (дд-мм-гггг): 17-09-2025

            Выберите действие;
            1 - Новая заметка;
            2 - Просмотреть все заметки;
            3 - Удалить заметку;
            4 - Выйти;

            Введите название операции: 2

            Ваш логин: Тихон
            Название заметки : Ситихи
            Описание заметки: Мороз и солнце
            Дата создания заметки: 27 - 01 - 2025
            Дата дэдлана(дд - мм - гггг); 17-09-2025
            До дэдлайна осталось 233 дней.

Цель №5 Удаление заметок

Решение: 1.2.5 delete_note.py

Создав несколько заметок пользователь может выбрать команду ,,Удалить заметку ,,
На экран выводится все существующие заметки , пользователю предлогается ввсести
,,имя пользоваетля ,,  или ,, заголовок заметки ,, который он желает удалить .
После ввода предлогается удалить найденную замтетку с таким же именем пользователя или заголовком.
Если пользоваткль не хочет удалять заметку цикл повторится , пример ;

            Текущие заметки:
            [{'username': 'Павел', 'title': 'Дела на завтра', 'content': 'Помыть посуду, сделать уроки,'
             ' в бассейн к 18:30', 'status': 'В процессе', 'created_date': '11-01-25', 'issue_date': '12-01-25'},
             {'username': 'Павел', 'title': 'Дела на послезавтра', 'content': 'вынести мусор, погулять с собакой',
              'status': 'В процессе', 'created_date': '11-01-25', 'issue_date': '12-01-25'},
             {'username': 'Николай', 'title': 'Учеба', 'content': 'Взять книги в библиотеке', 'status':
                 'В процессе', 'created_date': '11-01-25', 'issue_date': '20-01-25'}]
            Введите имя пользователя или заголовок заметки которую желаете удалить: павел
            Найдены следующие заметки:
            dict_items([('username', 'Павел'), ('title', 'Дела на завтра'),
                        ('content', 'Помыть посуду, сделать уроки, ''в бассейн к 18:30'), ('status', 'В процессе'),
                        ('created_date', '11-01-25'), ('issue_date','12-01-25')])
            Найдены следующие заметки:
            dict_items([('username', 'Павел'), ('title', 'Дела на послезавтра'),
                        ('content', 'вынести мусор, погулять с собакой'),
                        ('status', 'В процессе'), ('created_date', '11-01-25'),
                        ('issue_date', '12-01-25')])
            Желаете удалить все найденые заметки? "да" "нет": нет
            Введите заголовок заметки которую желаете удалить:

