##########################################################
# 🧩 MINI PROJECT: Student–Course Management System
# Goal: Practice classes, objects, and relationships in Python
# Concept Focus: __init__, encapsulation, validation, and composition
##########################################################

# ===============================
# STEP 1️⃣: Create the Student class
# ===============================

# 🔹 CLUE:
# Each student has: name, ID, and year (e.g., freshman, sophomore, junior, senior)
# Use __init__() to set them, and add getter/setter methods for safe data access.

class Student:
    def __init__(self, sn, sid, sy):
        # TODO 1: assign parameters to instance variables (use self)
        # Example: self.sname = sn
        self.sName = sn
        self.sId = sid
        self.sYear = sy

    # TODO 2: define getSName(), getSid(), and getSYear() to return each value
    def getSName(self):
        return self.sName

    def getSid(self):
        return self.sId

    def getSYear(self):
        return self.sYear

    # TODO 3: define setSYear(self, sy)
    # → check if sy is one of: freshman, sophomore, junior, senior
    # → if invalid, print a warning message
    def setSYear(self, sy):
        if type(sy) is str and (sy.lower() == "freshman" or sy.lower() == "sophomore" or sy.lower() == "junior" or sy.lower() == "senior"):
            self.syear = sy
        else:
            print("You have input an invalid value! The only allowable input are freshman, sophomore, junior, and senior")


# ===============================
# STEP 2️⃣: Create the Course class
# ===============================

# 🔹 CLUE:
# Each course has: course name, course ID, and a list of enrolled students.
# Add functions to display info and add students safely (type check + duplicates).

class Course:
    def __init__(self, cn, cid, sl):
        # TODO 4: assign cname, cid, slist to self variables
        self.cName=cn
        self.cId =  cid
        self.sList = sl

    def getCName(self):
        return self.cName

    def getCid(self):
        return self.cId

    # TODO 5: Define printAllStudents()
    # → Loop through self.slist and print each student’s info (name, id, year)
    def printAllStudents(self):
        for i in self.sList:
            print(f"name: {i.getSName}")

    # TODO 6: Define addStudent(st)
    # → Check if 'st' is a Student object using isinstance()
    # → Prevent adding the same student twice
    # → Append valid students to the list
    def addStudent(self, st):
        pass


# ===============================
# STEP 3️⃣: Create Objects and Test
# ===============================

# 🔹 CLUE:
# Create one course and three students, then add them to the course and print results.

# TODO 7: Create one Course object, e.g.
# c1 = Course("Python Programming", 13879007, [])

# TODO 8: Create three Student objects (freshman/junior/etc.)
# s1 = Student("John", 100, "Freshman")
# s2 = Student("David", 101, "Freshman")
# s3 = Student("Betty", 102, "Junior")

# TODO 9: Add all students to the course using addStudent()
# c1.addStudent(s1)
# c1.addStudent(s2)
# c1.addStudent(s3)

# TODO 10: Print all students using printAllStudents()


