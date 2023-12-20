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
