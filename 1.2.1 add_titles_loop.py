
notes = []

def new_note () :
    note = {
        "user_name": input("Ваш логин:"),
        "name_note": input(f"Название заметки : "),
        "description_note": input("Описание заметки: "),
        "deadline_note": input("Дэдлан заметки (дд-мм-гггг): ")

            }
    
    return note


while True :
    print("Выберите действие; \n"
          "1 - Новая заметка; \n"
          "2 - Просмотреть все заметки; \n"
          "3 - Удалить заметку; \n"
          "4 - Выйти; \n"
          )
    operator = input("Введите название операции: ")
    if operator == "1":
        notes.append( new_note())
        continue
    elif operator == "2":
        print(notes)
    elif operator == "3":
        notes.remove(note_remov())
    elif operator == "4":
        print(" Выход.")
        break
