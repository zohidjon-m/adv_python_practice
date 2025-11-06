# Write a function that takes a list of student
# names and grades, returns a tuple of
# (highest_grade, student_name).
# Explain why a tuple is a good return type here.

students  = [["Sam","Alice", "John", "Ali"],[[99,82,92],[78,90,67],[78,90,54],[89,87,78]]]
print(students)
# sam, grades = students[0][0], students[1][0]
# print(sam,grades)
def top_student(students):
    names = students[0]
    grades = students[1]
    max_grade = -1
    top_student = ""
    for grade in grades:
        st_gr = max(grade)
        if st_gr>max_grade:
            max_grade = st_gr
            top_student = names[grades.index(grade)]
    return (top_student,max_grade)
top_st = top_student(students)
print(f"Top student is {top_st[0]} with {top_st[1]} grade")