import os
os.system('cls')
schoolName= str(input(" Enter the organization name:  "))
print(f"Welcome {schoolName}\n\n")
totalstudent = int(input("Enter the total number of student :\n  "))

def studentInfo():
    print (f" The data is taken for {i+1} sutdent ")
    studentName=(str(input("Enter the name of student :  ")))
    studentClass = int(input("Enter the class of  student :  "))
    studentRoll = int(input(' Enter the roll number of student:  '))
    output1(studentName,studentClass,studentRoll)

def output1(studentName,studentClass,studentRoll):
    print(f" The name of {i+1} student is {studentName} .")
    print(f"The  class of {i+1} student is {studentClass}")
    print(f"The roll of {i+1} student is {studentRoll}")

def output2(totalMarks,totalSubject):
    print(f" The total marks of student is {totalMarks}")
    percentage = totalMarks//totalSubject
    print(f"The percentage of student is { percentage}")
    if percentage >= 90 and percentage <=100:
        print(" You got  A+")
    elif percentage >= 80 and percentage <90:
        print(" You got  A")
    elif percentage >= 70 and percentage <80:
        print(" You got  B+")
    elif percentage >= 60 and percentage <70:
        print(" You got  B")
    elif percentage >= 50 and percentage <60:
        print(" You got  C+")
    elif percentage>= 40 and percentage < 50:
        print("You got C.")
    else:
        print("You are fail in examination.")
       
        


marks=[]
for i in range(totalstudent):
    studentInfo() 
    totalSubject=(int (input('Enter the total subject :  ')  ))
    for j in range(totalSubject):
        marks.append(int(input (f"Enter the marks of  {j+1} subject :  ")))
    totalMarks= sum(marks)
    output2(totalMarks,totalSubject)
    
        

