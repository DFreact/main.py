import os.path

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
marks = []
gpa = {}

# for i in grades:
#     sum = 0
#     len = 0
#     for j in i:
#         sum += j
#         len += 1
#
#     average = sum / len

for i in range(len(grades)):
    length = len(grades[i])
    summary = sum(grades[i])
    average = summary / length


# /////// так код весит чуть больше ///////#
    marks.append(average)


print(marks)


for keys in sorted(students):
    gpa[keys] = marks[sorted(students).index(keys)]


print(gpa)

print(os.path.getsize("main.py"))