import pandas as pd 
import numpy as np 
# Student Details
name = input("Enter Student Name:")
roll_no = input("Enter Roll Number:")
# Subject Marks
subjects = ["Python", "DBMS", "PWC", "HV", "ISM"]
marks = []
for subject in subjects:
    mark = float(input(f"Enter marks in {subject}:"))
    marks.append(mark)
# Calculations
total = np.sum(marks)
percentage = np.mean(marks)
#Resut Calculation
if any (mark < 33 for mark in marks):
    result = "Fail"
    grade = "F"
elif percentage >= 90:
    result = "Pass"
    grade = "A+"
elif percentage >= 75:
    result = "Pass"
    grade = "A"
elif percentage >= 60:
    result = "Pass"
    grade = "B"
elif percentage >= 45:
    result = "pass"
    grade = "C"
else:
    result = "pass"
    grade = "D"
#Create DataFrame
data = {
    "Subject": subjects,
    "Marks": marks
}
df = pd.DataFrame(data)
# Display Result 
print("\n===== STUDENT RESULT REPORT =====")
print("Student Name:", name)
print("Roll Number:", roll_no)
print("\nSubject-wise Marks:")
print(df)
print("\nTotal Marks:", total, "/500")
print("percentage:", percentage, "%")
print ("Grade:", grade)
print("Final Result:", result)
