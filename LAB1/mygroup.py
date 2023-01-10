from statistics import mean
avg_mark = float(input())

def sort_students(students, avg_mark):
    for i in range(5):
        student = students[i]
        mark = mean(student['marks'])
        if (mark > avg_mark):
          print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))  

groupmates = [
    {
        "name": "Сергей",
        "surname": "Ковач",
        "exams": ["Иностранный язык", "РЯиКР", "Математический анализ"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Максим",
        "surname": "Нестеренко",
        "exams": ["Социология", "АиГ", "ТВиМС"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Елизавета",
        "surname": "Сенцова",
        "exams": ["Философия", "Физика", "ТЭЦ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Руслан",
        "surname": "Евдокимов",
        "exams": ["Линейная алгебра", "ОиБ", "РВС"],
        "marks": [2, 3, 3]
    },
    {
        "name": "София",
        "surname": "Сидорова",
        "exams": ["История", "Электроника", "Дискретная математика"],
        "marks": [5, 5, 4]
    }
]

sort_students(groupmates, avg_mark)