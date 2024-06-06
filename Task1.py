grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = sorted(list(students))
average_grades = []
for i in range(len(grades)):
    average_grades.append(sum(grades[i]) / len(grades[i]))

average_grades_dict = dict(zip(students_list, average_grades))

print(average_grades_dict)
