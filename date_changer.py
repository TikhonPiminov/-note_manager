import datetime

created_date = datetime.date.today()
#получаем текущую дату

print(f"Дата создания заметки в формате \"дд-мм-гггг\": {created_date.strftime("%d-%m-%Y")}")
#выводим текущую дату в нужном формате

issue_date=input("Дата истечения заметки (дедлайн) в формате \"дд-мм-гггг\": ")
#получаем от пользователя дату в формате дд-мм-гггг

issue_date=datetime.datetime.strptime(issue_date, "%d-%m-%Y")
#конвертируем строку с датой в объект