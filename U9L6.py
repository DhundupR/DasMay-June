

import mysql.connector








def getTeacherName(TeacherID):
   connection = mysql.connector.connect(user='dhundupr2',
                                        password='233048966',
                                        host='10.8.37.226',
                                        database='dhundupr2_db')
   cursor = connection.cursor()
   query = "select TeacherName from Teacher where TeacherID = "+TeacherID+""
   cursor.execute(query)
   for row in cursor:
       teacher=row;
   cursor.close()
   connection.close()
   return teacher;




def getResults(StudentID):
   connection = mysql.connector.connect(user='dhundupr2',
                                        password='233048966',
                                        host='10.8.37.226',
                                        database='dhundupr2_db')
   cursor = connection.cursor()
   query = "select Period, Room,CourseName,TeacherID from (select OfferedCourseID from Roster where StudentID = "+StudentID+") as c inner join OfferedCourse on c.OfferedCourseID = OfferedCourse.OfferedCourseID group by c.OfferedCourseID order by Period"
   cursor.execute(query)
   OfferedCourseList = []
   for row in cursor:
       OfferedCourseList.append(row)
   cursor.close()
   connection.close()


   return OfferedCourseList


def printTeacher(TeacherID):
    connection = mysql.connector.connect(user='dhundupr2',
                                         password='233048966',
                                         host='10.8.37.226',
                                         database='dhundupr2_db')
    cursor = connection.cursor()
    TeachersID = str(TeacherID)
    query2 = "call TeacherByID( " +  TeachersID + ")"
    cursor.execute(query2)
    teacherName = ""
    for rows in cursor:
        teacherName = rows
    cursor.close()
    connection.close()
    return teacherName[0]



studentID = input("Enter A Student ID: ")
result = getResults(studentID)
print(result)
for row in result:
    print("Period:", row[0])
    print("Course:", row[2])
    print("Room:", row[1])
    teacherName = printTeacher(row[3])
    print("Teacher:", teacherName)
    print("")





