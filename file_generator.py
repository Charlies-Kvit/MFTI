import csv
from random import randint, choice


def file_generator():
    """
    Создает файл с рандомным контентом для выполнения заданий
    :return:
    """
    string = 'АБВГД'
    data = """Сергеев Лука Донатович
    Владимиров Артем Леонидович
    Фролов Даниил Протасьевич
    Пахомов Матвей Петрович
    Романов Ибрагил Глебович
    Морозов Богдан Геннадиевич
    Крюков Клим Германнович
    Горшков Рубен Федорович
    Рогов Ростислав Евсеевич
    Копылов Роберт Серапионович"""
    data = data.split('\n    ')
    file_content = ['id Name titleProject_id class score'.split()]
    for index, name in enumerate(data):
        file_content.append([index, name, index, str(choice([10, 11])) + choice(string), choice([randint(1, 5),                                                                          None])])
    with open('students.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
        writer.writerows(file_content)
