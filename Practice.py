
num_students = input("How many students are you registering?"))
student_names = ""
i = 0

with open("student_list.txt", "w") as names_file, with open('reg_form.txt', 'w') as id_files:
        for i in range (0, num_students):
            student_names = input("Enter name of student:" )
            names_file.write(student_names + "\n")
            student_id = input("Please type in their ID number:")
            file2.write(f"{student_id} + '...............................' +'\n')
            i += 1
