import csv


def read_csv_file(filename: str, encoding: str) -> list[list[str]]:
    with open(filename, encoding=encoding) as file:
        reader = csv.reader(file)
        data = list()
        for el in reader:
            data.append(el)
    return data
