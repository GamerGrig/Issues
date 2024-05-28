grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_upd = sorted(list(students))

aaron_grades = sum(grades[0]) / len(grades[0])
bilbo_grades = sum(grades[1]) / len(grades[1])
johnny_grades = sum(grades[2]) / len(grades[2])
khendrik_grades = sum(grades[3]) / len(grades[3])
steve_grades = sum(grades[4]) / len(grades[4])


average_grades = {}
average_grades[students_upd[0]] = aaron_grades
average_grades[students_upd[1]] = bilbo_grades
average_grades[students_upd[2]] = johnny_grades
average_grades[students_upd[3]] = khendrik_grades
average_grades[students_upd[4]] = steve_grades
print(average_grades)