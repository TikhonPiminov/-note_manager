

# Примеры функций для работы с заметками
def create_note():
    print("Новая заметка создана!")

def display_notes():
    print("Список всех заметок:")

def update_note():
    print("Заметка обновлена!")

def delete_note():
    print("Заметка удалена!")

def search_notes():
    print("Поиск заметок выполнен!")

# Функция для отображения меню
def show_menu():
    print("\nМеню действий:")
    print("1. Создать новую заметку")
    print("2. Показать все заметки")
    print("3. Обновить заметку")
    print("4. Удалить заметку")
    print("5. Найти заметки")
    print("6. Выйти из программы")

# Основная программа
def main():
    while True:
        # Отображаем меню
        show_menu()

        # Получаем выбор пользователя
        choice = input("\nВаш выбор: ")

        # Обрабатываем выбор
        if choice == "1":
            create_note()
        elif choice == "2":
            display_notes()
        elif choice == "3":
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            search_notes()
        elif choice == "6":
            print("Программа завершена. Спасибо за использование!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")

# Запуск программы
if __name__ == "__main__":
    main()