import csv


def read_csv_file(filename: str, encoding: str) -> list[list[str]]:
    """
    Функция возвращает данные csv файла в виде матрицы
    :param filename:
    :param encoding:
    :return:
    """
    with open(filename, encoding=encoding) as file:
        reader = csv.reader(file)
        data = list()
        for el in reader:
            data.append(el)
    return data


def get_score(score: str) -> int:
    """
    Возвращает оценку в виде числа - int объекта
    :param score:
    :return:
    """
    if score:
        return int(score)
    else:
        return 0


def get_students_dict_project() -> dict:
    """
    Возвращает словарь, где ключом является id проекта, а значение - словарь с соответствующим содердимым
    id - айди ученика
    name - ФИО ученика
    class - класс ученика
    score - оценка за проект
    :return:
    """
    data = read_csv_file('students.csv', encoding='utf-8')
    answer = {}
    for row in data[1:]:
        answer[int(row[2])] = {'id': row[0], 'name': row[1], 'class': row[-2], 'score': row[-1]}
    return answer
