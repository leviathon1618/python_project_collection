
def readStudentInfo():
    Name = str(input("what is your name? "))
    studentID = int(input("what is your student ID? "))

    return Name,studentID

def readStudentGrades():
    GPA1 = float(input("grades for your first grade "))
    GPA2 = float(input("grades for your second grade "))
    GPA3 = float(input("grades for your third grade "))

    return GPA1,GPA2,GPA3