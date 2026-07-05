students = []
while True:
    print("===============================================")
    print("           STUDENT MANAGEMENT SYSTEM")
    print("===============================================")

    print("1. add students")
    print("2.view students")
    print("3.search students")
    print("4.update students")
    print("5.delete student")
    print("6.exit")


    choice = input("enter your choice:")

    if choice == "1":
        
        name=input("enter your name:")
        roll_no=input("enter your roll number:")
        age=input("enter your age:")
        course=input("enter your course:")
    
        student = {
            "name": name,
            "roll_no": roll_no,
            "age": age,
            "course": course
        }
        students.append(student)
        print(students)
        print("\nStudent added successfully!")

        print("________________student details__________________")
        print("name:", name)
        print("roll_no:", roll_no)
        print("age:", age)
        print("course:", course)

    elif choice == "2":

        if len(students)==0:
            print("no students found")

        else:
            for student in students:
                print("\n___________________________________________")
                print("Name:",student["name"])
                print("Roll_no:",student["roll_no"])
                print("age:",student["age"])
                print("course:",student["course"])

    elif choice == "3":
        search_roll = input("enter the roll_no to search:")

        found = False

        for student in students:
                if student["roll_no"] == search_roll :
                    print("\n___________________________________________")
                    print("Name:",student["name"])
                    print("Roll_no:",student["roll_no"])
                    print("age:",student["age"])
                    print("course:",student["course"])

                    found = True
                    break
        
        if found == False :
            print("roll_no not found.")

    elif choice == "4":
        update_roll = input("enter the roll_no to update:")

        found = False

        for student in students:
                if student["roll_no"] == update_roll :
                    print("\n___________________________________________")
                    new_name=input("enter your new_name:")
                    new_age=input("enter your new_age:")
                    new_course=input("enter your new_course:")

                    student["name"] = new_name
                    student["age"] = new_age
                    student["course"] =new_course

                    print("student updated successfully!")
                    found = True
                    break

        if found == False:
             print("roll number not found.")

    
    elif choice == "5":
        delete_roll = input("enter the roll_no to delate:")

        found = False

        for student in students:
                if student["roll_no"] == delate_roll :
                     students.remove(student)
                     print("student deleted successfully")
                     found = True
                     break
        if found == False:
             print("roll number not found.")
             
    elif choice == "6":
        print("thankyou for visiting student management portal")
        break
    else :
        print("invalid choice")
