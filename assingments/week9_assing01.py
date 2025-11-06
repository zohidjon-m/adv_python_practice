# Assignment 1 – Student–Course Management

class Student:
    def __init__(self, sid, sname, syear, gpa):
        self.sid = sid
        self.sname = sname
        self.syear = syear
        self.gpa = gpa

    def displayInfo(self):
        print(f"ID: {self.sid}, Name: {self.sname}, Year: {self.syear}, GPA: {self.gpa:.2f}")

    def updateGPA(self, new_gpa):
        if 0 <= new_gpa <= 4.5:
            self.gpa = new_gpa
            print(f"{self.sname}'s GPA updated to {self.gpa:.2f}")
        else:
            print("Invalid GPA. Must be between 0.0 and 4.5")

class Course:
    def __init__(self, cname, cid):
        self.cname = cname
        self.cid = cid
        self.student_list = []

    def addStudent(self, student):
        if isinstance(student, Student):
            for s in self.student_list:
                if s.sid == student.sid:
                    print(f"Student {student.sname} already enrolled.")
                    return
            self.student_list.append(student)
            print(f"{student.sname} added to {self.cname}.")
        else:
            print("Error: Only Student objects can be added.")

    def removeStudent(self, student):
        for s in self.student_list:
            if s.sid == student.sid:
                self.student_list.remove(s)
                print(f"{s.sname} removed from {self.cname}.")
                return
        print("Student not found.")

    def printCourseReport(self):
        print(f"\nCourse Report - {self.cname} ({self.cid})")
        for s in self.student_list:
            s.displayInfo()


s1 = Student(1001, "Aylin", "Freshman", 3.7)
s2 = Student(1002, "David", "Junior", 3.9)
s3 = Student(1003, "Nora", "Senior", 4.2)

course = Course("Advanced Python Programming", "CSE 0102")
course.addStudent(s1)
course.addStudent(s2)
course.addStudent(s3)

s2.updateGPA(4.3)
course.printCourseReport()
