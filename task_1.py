import csv

from functions import read_csv_file, get_score


def find_score(name: str) -> str:
    """
    Функция возращает оценку ученика, на вод подается имя или фамилия или и то и другое на вход
    (в рамках данной задачи ФИ)
    :param name:
    :return:
    """
    data = read_csv_file('students.csv', encoding='utf-8')
    for row in data[1:]:
        if name in row[1]:
            score = get_score(row[-1])
            return f'Ты получил: {score}, за проект - {row[2]}'


def get_average_score():
    """
    Создает и записывает в файл среднее значение баллов для каждого класса
    :return:
    """
    data = read_csv_file('students.csv', encoding='utf-8')
    finally_data = {}
    for row in data[1:]:
        if row[-2] in finally_data:
            score = get_score(row[-1])
            finally_data[row[-2]].append(int(score))
        else:
            score = get_score(row[-1])
            finally_data[row[-2]] = [score]
    with open('student_new.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
        writer.writerow(['class', 'average_score'])
        for el in finally_data:
            writer.writerow([el, round(sum(finally_data[el]) / len(finally_data[el]), 3)])
