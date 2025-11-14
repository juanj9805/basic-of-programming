# MY VERSION

import time

number_of_students = int(input("How many students are there on the classroom: "))

def sum_notes_students(students):
    students_notes = []
    for student in range(students):
        print(f"Enter the notes of the student number {student+1}:")
        student_ID = time.time()
        student_name = input("Enter the name of the student: ")
        student_note_1 = float(input("Enter the first note: "))
        student_note_2 = float(input("Enter the second note: "))
        student_note_3 = float(input("Enter the third note: "))
        average_note = (student_note_1 + student_note_2 + student_note_3)/3
        print(f"{"-"*50}")
        student_info = {    
            "student_ID": student_ID,
            "student_name": student_name,
            "student_note_1": student_note_1,
            "student_note_2": student_note_2,
            "student_note_3": student_note_3,
            "average_note": average_note,
        }
        print(average_note)
        print("-"*50)
        students_notes.append(student_info)
    return students_notes 

# print(sum_notes_students(number_of_students))

def calification(notes):
    aprobed = []
    reprobed = []
    for note in notes:
        if note["average_note"] >=0 and note["average_note"] <=5:
            if note["average_note"]>=3:
                aprobed.append(note["average_note"])
            else:
                reprobed.append(note["average_note"])
    return [aprobed,reprobed]



print(calification(sum_notes_students(number_of_students)))

# CHATGPT VERSION

import uuid

def sum_notes_students(students):
    """Registers students and calculates their average grade."""
    students_notes = []

    for student in range(students):
        print("-" * 50)
        print(f"Enter the notes of student number {student + 1}:")
        student_ID = uuid.uuid4()
        student_name = input("Enter the name of the student: ")

        try:
            note1 = float(input("Enter the first note: "))
            note2 = float(input("Enter the second note: "))
            note3 = float(input("Enter the third note: "))
        except ValueError:
            print("⚠️ Invalid input — skipping this student.")
            continue

        average = (note1 + note2 + note3) / 3

        student_info = {
            "student_ID": student_ID,
            "student_name": student_name,
            "notes": [note1, note2, note3],
            "average_note": average,
        }

        print(f"{student_name}'s average: {average:.2f}")
        print("-" * 50)
        students_notes.append(student_info)

    return students_notes


def classify_students(students_notes):
    """Separates students into approved and failed lists based on their average."""
    APPROVED_LIMIT = 3.0
    MIN_GRADE, MAX_GRADE = 0, 5

    approved = []
    failed = []

    for student in students_notes:
        avg = student["average_note"]
        if MIN_GRADE <= avg <= MAX_GRADE:
            if avg >= APPROVED_LIMIT:
                approved.append(student)
            else:
                failed.append(student)
        else:
            print(f"⚠️ Invalid average for {student['student_name']}: {avg}")

    return approved, failed


def show_results(approved, failed):
    """Prints a summary of approved and failed students."""
    print("\n" + "=" * 50)
    print(f"✅ APPROVED STUDENTS ({len(approved)}):")
    for s in approved:
        print(f"- {s['student_name']} ({s['average_note']:.2f})")

    print("\n❌ FAILED STUDENTS ({len(failed)}):")
    for s in failed:
        print(f"- {s['student_name']} ({s['average_note']:.2f})")
    print("=" * 50)


# Main program
number_of_students = int(input("How many students are there in the classroom: "))
students_data = sum_notes_students(number_of_students)
approved, failed = classify_students(students_data)
show_results(approved, failed)

# SUMMARY OF IMPROVEMENTS

# | **Problem**                                                             | **Fix**                                                             | **Why**                                                                                     |
# | ----------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
# | `print(f"{"-"*50}")` → ❌ invalid syntax                                | Escape quotes: `print(f'{"-"*50}')` **or** simply `print("-" * 50)` | Double quotes inside f-strings cause syntax errors                                          |
# | You use `time.time()` for IDs                                           | Use `uuid.uuid4()`                                                  | `time.time()` can create duplicate IDs if inputs are too fast; UUIDs are universally unique |
# | You don’t handle invalid input (letters, etc.)                          | Add `try/except` for numeric conversion                             | Prevents crashes when the user types non-numeric data                                       |
# | You use `int()` for notes                                               | Use `float()`                                                       | Allows decimal grades like `3.5` instead of forcing integers                                |
# | You check `if note["average_note"] >= 0 and note["average_note"] <= 5:` | Define constants like `MIN_GRADE = 0`, `MAX_GRADE = 5`              | Makes your code easier to read and maintain                                                 |
# | You only store `average_note` in `aprobed` and `reprobed` lists         | Store full `student_info` dicts                                     | Helps identify *who* passed or failed, not just the score                                   |
# | `calification()` could have clearer naming                              | Rename to `classify_students()`                                     | “Calification” isn’t standard English; “classification” or “evaluation” fits better         |
# | No summary printed                                                      | Print a clear report of approved vs failed                          | Improves UX and readability                                                                 |
