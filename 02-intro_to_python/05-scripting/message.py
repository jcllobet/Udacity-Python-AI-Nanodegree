names =  str(input("Enter student names: ")) # get and process input for a list of names
assignments = str(input("Enter their assignments: ")) # get and process input for a list of the number of assignments
grades =  str(input("Enter their grades: ")) # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"



# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
names_list = names.split(",")
assignments_list = assignments.split(",")
grades_list = grades.split(",")
max_grade = 0

for e in grades_list:
  if max_grade < int(e):
    max_grade = int(e)
  else:
    pass

for e in range(len(names_list)):

  print(message.format(names_list[e],assignments_list[e],grades_list[e],max_grade))
