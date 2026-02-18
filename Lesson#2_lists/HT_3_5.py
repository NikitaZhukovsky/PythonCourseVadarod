"""
Дан список оценок студентов [[5, 3, 4, 2, 5, 4, 3, 5, 4, 2].
Необходимо обработать этот список: удалить все неудовлетворительные оценки (меньше 4),
отсортировать оставшиеся по убыванию, затем добавить в начало списка среднее арифметическое этих оценок,
а в конец списка количество оставшихся оценок.
"""


grades_list = [5, 3, 4, 2, 5, 4, 3, 5, 4, 2]

good_grades = []

for grade in grades_list:
    if grade >= 4:
        good_grades.append(grade)

good_grades.sort(reverse=True)

good_grades.insert(0, sum(good_grades) / len(good_grades))
good_grades.append(len(good_grades) - 1)

print(f"Результат: {good_grades}")

