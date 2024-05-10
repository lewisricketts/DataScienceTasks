num_students = int(input("How many students are you registering?"))

# Open student_list.txt to append student names
with open('student_list.txt', 'a+') as names_file, open('reg_form.txt', 'a+') as id_files:
    for i in range(num_students):
        student_name = input("Enter name of student:")
        names_file.write(student_name + '\n')  # Write student name to student_list.txt
        student_id = input(f"Please type {student_name}'s ID number:")
        id_files.write(student_id  '.......................................\n')  # Write student ID to reg_form.txt

print("You have successfully added the relevant students")
