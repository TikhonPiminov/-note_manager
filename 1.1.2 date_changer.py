mport datetime

created_date = datetime.date.today()
issue_date=input("Дэдлайн заметки \"дд-мм-гггг\": ")
issue_date=datetime.datetime.strptime(issue_date, "%d-%m-%Y")
print(f"Дата создания: {created_date}, Дэдлайн: {issue_date} ")
