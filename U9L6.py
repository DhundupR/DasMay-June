
import mysql.connector




def getInput():
   while True:
       x = input("Are You Entering As A Student Or Teacher: s/t :  ")
       if x == "s":
           return x
       elif x == "t":
           return x
       else:
           print("Incorrect Input Try Again ('s' or 't' )")





def getTeacherName(TeacherID):
   connection = mysql.connector.connect(user='dhundupr2',
                                        password='233048966',
                                        host='10.8.37.226',
                                        database='dhundupr2_db')
   cursor = connection.cursor()
   query = "select TeacherName from Teacher where TeacherID = " + TeacherID + ""
   cursor.execute(query)
   for row in cursor:
       teacher = row;
   cursor.close()
   connection.close()
   return teacher;




def getStudentResults():
   StudentID = input("Enter A Student ID: ")
   connection = mysql.connector.connect(user='dhundupr2',
                                        password='233048966',
                                        host='10.8.37.226',
                                        database='dhundupr2_db')
   cursor = connection.cursor()
   query = "select Period, Room,CourseName,TeacherID from (select OfferedCourseID from Roster where StudentID = " + StudentID + ") as c inner join OfferedCourse on c.OfferedCourseID = OfferedCourse.OfferedCourseID group by c.OfferedCourseID order by Period"
   cursor.execute(query)
   OfferedCourseList = []
   for row in cursor:
       OfferedCourseList.append(row)
   cursor.close()
   connection.close()


   return OfferedCourseList


def getScheduleList(role):
   if role == "t":
       return TeacherSchedule();
   elif role == "s":
    studentMenu()

def TeacherSchedule():
    TeacherID = input("Enter A Teacher ID: ")
    teacher = getTeacherName(TeacherID)
    print("Welcome", teacher[0])
    connection = mysql.connector.connect(user='dhundupr2',
                                         password='233048966',
                                         host='10.8.37.226',
                                         database='dhundupr2_db')
    cursor = connection.cursor()
    query="select Period, Room, CourseName,TeacherID from (select * from OfferedCourse where TeacherID = "+TeacherID+") as c inner join Roster on c.OfferedCourseID = Roster.OfferedCourseID group by c.OfferedCourseID  order by Period;"
    cursor.execute(query)
    OfferedCourseList = []
    for row in cursor:
        OfferedCourseList.append(row)
    cursor.close()
    connection.close()
    return OfferedCourseList

def studentSchedulePrint(result):
    print("");
    for row in result:
        print("Period:", row[0])
        print("Course:", row[2])
        print("Room:", row[1])
        teacherName = printTeacher(row[3])
        print("Teacher:", teacherName)
        print("")
def studentMenu():
    while True:
        print("Enter a to Print Student Schedule: ")
        print("Enter g to print grades for a specific class: ")
        print("Enter q to quit: ")
        choice = input("Select: ")
        StudentChoice(choice)
        if choice == "q":
            print("Good Bye")
            break

def StudentChoice(input):
    while True:
        if input == "a":
            studentSchedulePrint(getStudentResults())
            break
        if input == "q":
            break
        print("Try Again")
def printTeacher(TeacherID):
   connection = mysql.connector.connect(user='dhundupr2',
                                        password='233048966',
                                        host='10.8.37.226',
                                        database='dhundupr2_db')
   cursor = connection.cursor()
   TeachersID = str(TeacherID)
   query2 = "call TeacherByID( " + TeachersID + ")"
   cursor.execute(query2)
   teacherName = ""
   for rows in cursor:
       teacherName = rows
   cursor.close()
   connection.close()
   return teacherName[0]





x = getInput()
result = getScheduleList(x)


