
notes = []

def new_note () :
    note = {                   #информация о заметке ввод
        "user_name": input("Ваш логин:"),
        "name_note": input(f"Заголвок заметки: "),
        "description_note": input("Описание заметки: "),
        "data_note": input("Дата создания (дд-мм-гггг): "),
        "deadline_note": input("Дэдлан заметки (дд-мм-гггг): ")


            }

    return notes


while True :           # возможные действия с заметкой
    print("Выберите действие; \n" 
          "1 - Новая заметка; \n"
          "2 - Просмотреть все заметки; \n"
          "3 - Выйти; \n"
          )
    operator = input("Введите название операции: ") # ввод выбранной операвции
    if operator == "1":
        notes.append( new_note())
        continue
    elif operator == "2":
        print(notes)
    elif operator == "3":
        print(" Выход.")
        break


