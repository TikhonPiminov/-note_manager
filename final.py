user = input("Введите как вас зовут: ")

import datetime
created_date = datetime.date.today()
print(f"Дата создания заметки в формате \"дд-мм-гггг\": {created_date.strftime("%d-%m-%Y")}")
issue_date=input("Дата истечения заметки (дедлайн) в формате \"дд-мм-гггг\": ")
issue_date=datetime.datetime.strptime(issue_date, "%d-%m-%Y")

notes_1 = input("Название заметки : ") , input("Описание заметки: ")

user_date = ["Имя пользователя:",user ,"Заметка и описание: ",notes_1,"Дедлайн заметки:", issue_date]
print(user_date)



