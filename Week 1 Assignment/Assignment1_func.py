# PROBLEM STATEMENT 1:
'''
EMPLOYEE SALARY CALCULATOR
'''

Employee_name = input("Enter employee name: ")
basic_salary = int(input("Enter basic salary: "))
hra = (20/100)*basic_salary
da = (10/100)*basic_salary
net_salary = basic_salary + hra + da

def salary_calculate(basic_salary):
  net_salary = basic_salary + hra + da
  return net_salary

print("HRA is:", hra)
print("DA is:", da)
print("Net Salary is:",  net_salary)

print("-------------")
print("")





#PROBLEM STATEMENT 2: CALCULATE STUDENT GRADE USING FUNCTIONS

def calculate_total(marks):
  return sum(marks)
def calculate_percentage(total, num_subjects):
  percentage = (total/(num_subjects*100))*100
  return percentage
def assign_grade(percentage):
  if percentage >= 90:
    grade = "A"
  elif percentage >= 75-89:
    grade = "B"
  elif percentage >= 60-74:
    grade = "C"
  elif percentage >= 40-59:
    grade = "D"
  else:
    grade = "F"
  return grade

Student_name = input("Student Name: ")
marks = []
for i in range(5):
  mark = float(input(f"Enter marks for subject {i+1}: "))
  marks.append(mark)

total = sum(marks)
percentage = calculate_percentage(total, len(marks))
final_grade = assign_grade(percentage)
print("Result is:")
print("Student Name:", Student_name)
print("Total Marks:", total)
print("Percentage:", percentage,"%")
print("Grade:", final_grade)