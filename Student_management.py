# Student management system in python

class Student: # Define a class named Student
    def __init__(self, name, age, grade): # The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
        # Create a class named Person, use the __init__() method to assign values for name and age:
        # initialize the properties of the class
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Extracting the student data from the file and storing it in a list
def load_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:                                      # for line in file: reads the file one line at a time.
                parts = line.strip().split(",")                    # line.strip().split(",") removes the newline and separates the record at commas.

                name = parts[0].replace("Name: ", "").strip()      # .replace("Name: ", "") removes the label "Name: " from the first part of the record.
                age = int(parts[1].replace("Age: ", "").strip())   # .replace("Age: ", "") removes the label "Age: " from the second part of the record and converts it to an integer.
                grade = parts[2].replace("Grade: ", "").strip()    # .replace("Grade: ", "") removes the label "Grade: " from the third part of the record.

                student = Student(name, age, grade)                # .Create a Student object with the extracted data
                all_students.append(student)

    except FileNotFoundError:
        print("No saved student records found.")


# line = "Name: Bright, Age: 20, Grade: A"

# parts = line.split(",") #  .split(",") separates the line at each comma.

# name = parts[0].replace("Name: ", "").strip()  # .replace("Name: ", "") removes the label.
# age = int(parts[1].replace("Age: ", "").strip())  # int() converts the age from text into an integer.
# grade = parts[2].replace("Grade: ", "").strip() # .strip() removes any leading or trailing whitespace.

all_students = []  # List to store all students

# Introducing File Handling



def introduction():
    print("\n")
    print("\t\t\t Welcome to the Student Management System")
    print("\t\t ------------------------------------------------------")
    print("\n")


    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    print("\n")

    choice = int(input("Enter your choice: "))
    return choice



def main_work():
    while True: 
        choicee = introduction()
        if choicee == 1:
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            grade = input("Enter student grade: ")
            student = Student(name, age, grade)
            all_students.append(student)
            with open("students.txt", "a") as file:
                file.write(str(student) + "\n")
            print("\nStudent added successfully!")
            print(student)
        
        elif choicee == 2:
            print("\nList of Students:")
            try:
                with open("students.txt", "r") as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print("No student data found.")
        elif choicee == 3:
            print("Exiting the Student Management System. Goodbye!")
            break
        







def main():
    load_students()  # Load existing students from the file
    main_work()

if __name__ == "__main__":
    main()







