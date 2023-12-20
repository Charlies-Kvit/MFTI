from functions import get_students_dict_project, get_score


def get_student_info(project_id: int, data: dict) -> str:
    """
    Возвращает отформатированную строку с найденными данными по ученику или же,
    если ничего не нашлось, возращает соответствующую строку.
    :param project_id:
    :param data:
    :return:
    """
    try:
        answer = data[project_id]
        name = answer['name'].split()
        score = get_score(answer['score'])
        return f"Проект № {project_id} делал: {name[1][0]}. {name[0]} он(а) получил(а) оценку - {score}"
    except KeyError:
        return f"Ничего не найдено"


def main():
    """
    Бесконечный цикл для взаимодействием с пользователем
    :return:
    """
    data = get_students_dict_project()
    search = ""
    while search != 'СТОП':
        search = input('Введите id проекта >> ')
        if not search.isdigit():
            print("Ошибка - вы ввели не число")
        else:
            print(get_student_info(int(search), data))
    print("Конец выполнения!")


if __name__ == '__main__':
    main()
