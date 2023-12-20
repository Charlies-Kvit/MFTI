from functions import read_csv_file

name = "Морозов Богдан"
data = read_csv_file('students.csv', encoding='utf-8')
for obj in data[1:]:
    if name in obj[1]:
        if obj[-1]:
            score = obj[-1]
        else:
            score = None
        print(f'Ты получил: {score}, за проект - {obj[2]}')
