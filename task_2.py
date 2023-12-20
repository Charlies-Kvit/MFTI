from functions import read_csv_file, get_score


def get_winners() -> str:
    """
    Функция сортирует участников и выводит три первых места среди 10-ыч классов
    :return:
    """
    data = read_csv_file('students.csv', encoding='utf-8')[1:]
    for index, el in enumerate(data):
        if index == 0:
            continue
        el_ind = index
        while el_ind != 0 and int(get_score(el[-1])) > int(get_score(data[el_ind - 1][-1])):
            data[el_ind] = data[el_ind - 1]
            data[el_ind - 1] = el
            el_ind -= 1
    winners = []
    for student in data:
        if '10' in student[-2]:
            name = student[1].split()
            winners.append(f"{name[1]} {name[0]}")
            if len(winners) == 3:
                break
    for index, el in enumerate(winners):
        winners[index] = f"{index + 1} место: {el}"
    winners.insert(0, '10 класс:')
    return "\n".join(winners)
