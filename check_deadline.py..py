from datetime import datetime


def days_until(target_date):
    current_date = datetime.now().date() # Задаем текущую дату
    target_date = datetime.strptime(target_date, '%d-%m-%Y').date() #Формат для даты дэдлайна
    days_left = (target_date - current_date).days # Вычиленией оставшихся дней до дэдлана 
    return days_left


created_date = datetime.today()
print(f"Дата создания заметки : {created_date.strftime("%d-%m-%Y")}") # Выыод текущей даты в нужном формате
target_date = input("Дата дэдлана (дд-мм-гггг); ")
print(f"До дэдлайна осталось {days_until(target_date)} дней.")# вывод дней до дэдлайна
