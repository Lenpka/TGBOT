from testtables import get_table_by_url, service_account, extract_data_from_sheet, test_get_data
import handlers.schedule
from collections import defaultdict
# Весь этот модуль стоит вынести в отдельный каталог

table_link_schedule = 'https://docs.google.com/spreadsheets/d/1GDyS3jw3tPuYKNxmjaSxGjQoRG2MqOOVpZRttTE7nnA/edit?gid=153533360#gid=153533360'

compareDays = {
    "Понедельник": "Monday",
    "Вторник": "Tuesday",
    "Среда": "Wednesday",
    "Четверг": "Thursday",
    "Пятница": "Friday",
    "Суббота": "Saturday",
}

def schedule_test_get_data() -> dict:
    """Принимает расписание"""
    # todo - read variables from env
    client = service_account(filename='./tgbot.json')
    tables = get_table_by_url(client, table_link_schedule)
    data = extract_data_from_sheet(tables, "1 бак.")
    schedule = defaultdict()
    schedule["Sunday"] = [
        handlers.schedule.Lesson(
            name = 'Выходной',
            time = '',
    )]
    day = ''
    time = ''
    name = ''

    for dat in data:
        if dat['День недели']:
            day = compareDays[dat["День недели"]]
            schedule[day] = []
        if dat['Время']:
            time = dat['Время']
        if dat['Учебная дисциплина']:
            name = dat['Учебная дисциплина']
        lesson = handlers.schedule.Lesson(
            name=name,
            time=time,
            teacher=dat['Преподаватель'],
            comment=dat['Комментарий'],
            place=dat['Аудитория'],
                     )
        schedule[day].append(lesson)
    return schedule
def homework_get_data() -> dict:
    client = service_account(filename='./tgbot.json')
    tables = get_table_by_url(client, table_link_schedule)
    data = extract_data_from_sheet(tables, "1 бак.")
    works = defaultdict()
    works["Sunday"] = [
        handlers.schedule.Lesson(
            name = 'Выходной',
            time = '',
    )]
    day = ''
    time = ''
    name = ''

    for dat in data:
        if dat['День недели']:
            day = compareDays[dat["День недели"]]
            works[day] = []
        if dat['Учебная дисциплина']:
            name = dat['Учебная дисциплина']
        lesson = handlers.schedule.Lesson(
            name=name,
            teacher=dat['Преподаватель'],
            task=dat['Домашнее задание']
                     )
        works[day].append(lesson)
    return works
if __name__ == "__main__":
    print(schedule_test_get_data())
