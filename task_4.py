import csv
from string import ascii_lowercase, ascii_uppercase, digits
from random import choice
from functions import read_csv_file


def generate_login(name: str) -> str:
    """
    Генирирует логин для пользователя по ФИО и возращает его
    :param name:
    :return:
    """
    name = name.split()
    return f"{name[0]}_{name[1][0]}{name[2][0]}"


def generate_password(length: int) -> str:
    """
    Генерирует пароль в соответствии правилом из задания:
    'пароль должен состоять из 8 символов, включать в себя заглавные,
    строчные буквы английского алфавита и цифры.'
    и  возращает его.
    :param length:
    :return:
    """
    choice_from = ascii_uppercase + ascii_lowercase + digits
    flag = True
    while flag:
        password = ''
        for i in range(length):
            password += choice(choice_from)
        upper_flag = False
        lower_flag = False
        digit_flag = False
        for el in password:
            if el in ascii_uppercase and upper_flag is False:
                upper_flag = True
            if el in ascii_lowercase and lower_flag is False:
                lower_flag = True
            if el in digits and digit_flag is False:
                digit_flag = True
        flag = not(upper_flag and lower_flag and digit_flag)
    return password


def create_student_file_with_login_password():
    """
    Создает новый файл и записывает туда старые данные, добавляя туда логин и пароль.
    :return:
    """
    data = read_csv_file('students.csv', encoding='utf-8')
    data[0] = ["id", "Name", "titleProject_id", "class", "score", "login", "password"]
    for index, row in enumerate(data[1:]):
        data[index + 1].extend([generate_login(row[1]), generate_password(8)])
    with open('students_password.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
        writer.writerows(data)
