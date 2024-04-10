import json

file_name = "course_data.json"

def clear_json_file():
    with open(file_name, "w") as file:
        json.dump({}, file)

try:
    with open(file_name, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {
        "grand_set_course_code": {},
        "grand_course_total_point": 0,
        "grand_course_total_credit": 0,
        "cgpa": 0
    }
except json.decoder.JSONDecodeError:
    # If the JSON file is empty or invalid, initialize with default data
    data = {
        "grand_set_course_code": {},
        "grand_course_total_point": 0,
        "grand_course_total_credit": 0,
        "cgpa": 0
    }

grade_def = {"AA": 4.0, "BA": 3.5, "BB": 3.0, "CB": 2.5, 
             "CC": 2.0, "DC": 1.5, "DD": 1.0, "FD": 0.5, 
             "FF": 0.0, "W": 0.0, "EX": 0.0, "S": 0.0, "NA": 0.0}

# Access data after loading or initializing it
grand_set_course_code = data.get("grand_set_course_code", {})
grand_course_total_point = data.get("grand_course_total_point", 0)
grand_course_total_credit = data.get("grand_course_total_credit", 0)
cgpa = data.get("cgpa", 0)

while True:
    print("*******************************************************************************************************")
    print("*Enter your course details below. Grades should be AA, BA, BB, CB, CC, DC, DD, FD, FF, W, EX or S.    *")
    print("*Type 'delete' in Course Grade to delete a course.                                                    *")
    print("*Type 'clear' in Course Code to clear all data.                                                       *")
    print("*Type 'show' in Course Code to show all data.                                                         *")
    print("*******************************************************************************************************")
    
    course_code = str(input("Enter Course Code: ")).upper()
    if course_code == "CLEAR":
        clear_json_file()
        grand_set_course_code = {}
        grand_course_total_point = 0
        grand_course_total_credit = 0
        cgpa = 0
        print("\nAll courses deleted.")
        continue
    
    if course_code == "SHOW":
        print("*******************************************************************************************************")
        print("*Course Details:", grand_set_course_code)
        print("-------------------------------------------------------------------------------------------------------")
        print("CGPA:", cgpa)
        print("Total Points:", grand_course_total_point)
        print("Total Credits:", grand_course_total_credit)
        print("-------------------------------------------------------------------------------------------------------")

        continue
    
    while True:
        try:
            course_credit = int(input("Enter Course Credit: "))
            if course_code in grand_set_course_code:
                old_course_credit = grand_set_course_code[course_code]["Course Credit"]
                if course_credit == old_course_credit:
                    break
                else:
                    print("\nCourse Credit cannot be updated. Please enter the same Course Credit.")
                    continue  # Döngüyü başa döndür
        except ValueError:
            print("\nInvalid input! Please enter a valid numeric Course Credit.")
            continue  # Döngüyü başa döndür
        else:
            break  # Hata yoksa döngüyü kır


                
    while True:
        course_grade = str(input("Enter Course Grade: ")).upper()
    
        if course_grade in grade_def or course_grade == "DELETE":
            break
        else:
            print("\nInvalid input! Please enter a valid Course Grade.")

    
    if course_grade == "DELETE":
        if course_code in grand_set_course_code:
            old_course_grade = grand_set_course_code[course_code]["Course Grade"]
            course_grade = grade_def[old_course_grade]  
            course_point = grand_set_course_code[course_code]["Course Point"]
            del grand_set_course_code[course_code]
            grand_course_total_point -= course_point
            grand_course_total_credit -= course_credit
            print("\nCourse deleted.")
        else:
            print("\nCourse code not found. No course deleted.")
    else:
        course_point = course_credit * grade_def[course_grade]
        course = {"Course Credit": course_credit, "Course Grade": course_grade, "Course Point": course_point}

        if course_code in grand_set_course_code:
            grand_course_total_point -= grand_set_course_code[course_code]["Course Point"]
            grand_course_total_credit -= grand_set_course_code[course_code]["Course Credit"]
            print("\nCourse already exists. It is updated.")

        grand_set_course_code[course_code] = course
        grand_course_total_point += course_point
        grand_course_total_credit += course_credit
        print("\nCourse added.")

    if grand_course_total_credit == 0:
        cgpa = 0
    else:
        cgpa = float(grand_course_total_point / grand_course_total_credit)

    print("*******************************************************************************************************")
    print("Course Details:", grand_set_course_code)
    print("-------------------------------------------------------------------------------------------------------")
    print("CGPA:", cgpa)
    print("Total Points:", grand_course_total_point)
    print("Total Credits:", grand_course_total_credit)
    print("-------------------------------------------------------------------------------------------------------")


    data = {
        "grand_set_course_code": grand_set_course_code,
        "grand_course_total_point": grand_course_total_point,
        "grand_course_total_credit": grand_course_total_credit,
        "cgpa": cgpa
    }
    with open(file_name, "w") as file:
        json.dump(data, file)