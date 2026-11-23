# CASE STUDY 3: Smart Student Course Registration System
# Concepts: strings, lists, tuples and sets

available_courses = {
    "CS101": "Python Programming",
    "CS102": "Computer Networks",
    "CS103": "Database Management",
    "CS104": "Operating Systems",
    "CS105": "Cyber Security",
    "MA101": "Engineering Mathematics"
}

print("=" * 60)
print("        SMART STUDENT COURSE REGISTRATION SYSTEM")
print("=" * 60)

student_id = input("Enter Student ID: ").strip().upper()
student_name = input("Enter Student Name: ").strip().title()
branch = input("Enter Branch: ").strip().upper()
semester = input("Enter Semester: ").strip()

# Tuple stores fixed/immutable student details.
student_details = (student_id, student_name, branch, semester)

print("\nAvailable courses:")
for code, course_name in available_courses.items():
    print(f"{code} - {course_name}")

# List stores the courses entered by the student.
selected_courses = []

while True:
    course_code = input(
        "\nEnter course code (or type DONE to finish): "
    ).strip().upper()

    if course_code == "DONE":
        break

    # Validate code using string operations and dictionary membership.
    if not (course_code.startswith(("CS", "MA")) and course_code[2:].isdigit()):
        print("Invalid course-code format.")
        continue

    if course_code not in available_courses:
        print("Course code does not exist.")
        continue

    selected_courses.append(course_code)
    print("Course added:", available_courses[course_code])

# Set removes duplicate course selections.
unique_courses = set(selected_courses)

print("\n" + "=" * 60)
print("                 REGISTRATION SUMMARY")
print("=" * 60)
print("Student ID :", student_details[0])
print("Name       :", student_details[1])
print("Branch     :", student_details[2])
print("Semester   :", student_details[3])

print("\nCourses entered (list):")
if selected_courses:
    for index, code in enumerate(selected_courses, start=1):
        print(f"{index}. {code} - {available_courses[code]}")
else:
    print("No courses selected.")

print("\nFinal registered courses (duplicates removed):")
if unique_courses:
    for index, code in enumerate(sorted(unique_courses), start=1):
        print(f"{index}. {code} - {available_courses[code]}")
else:
    print("No courses registered.")

print("\nTotal selections :", len(selected_courses))
print("Unique courses   :", len(unique_courses))
print("=" * 60)
