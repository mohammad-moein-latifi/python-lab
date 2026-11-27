"""Console-based student grade management system."""

CONDITIONAL_GPA_LIMIT = 12.0
MIN_GRADE = 0.0
MAX_GRADE = 20.0


def read_non_empty_text(prompt):
    """Read text that must not be empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_integer(prompt, minimum=None):
    """Read an integer, optionally enforcing a minimum value."""
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if minimum is not None and value < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue

        return value


def read_grade(prompt):
    """Read a grade between MIN_GRADE and MAX_GRADE."""
    while True:
        raw_value = input(prompt).strip()
        try:
            grade = float(raw_value)
        except ValueError:
            print("Please enter a valid number (use a dot for decimals).")
            continue

        if not MIN_GRADE <= grade <= MAX_GRADE:
            print(f"Grade must be between {MIN_GRADE:g} and {MAX_GRADE:g}.")
            continue

        return grade


def calculate_gpa(student):
    """Calculate a student's unit-weighted GPA."""
    total_units = sum(course["units"] for course in student["courses"])
    if total_units == 0:
        return None

    weighted_total = sum(
        course["grade"] * course["units"]
        for course in student["courses"]
    )
    return weighted_total / total_units


def add_student(students):
    """Collect a student and at least one course."""
    print("\n--- Add Student ---")
    first_name = read_non_empty_text("First name: ")
    last_name = read_non_empty_text("Last name: ")

    courses = []
    while True:
        print("\nEnter course information:")
        course_name = read_non_empty_text("Course name: ")
        units = read_integer("Course units: ", minimum=1)
        grade = read_grade("Grade (0-20): ")

        courses.append({
            "name": course_name,
            "units": units,
            "grade": grade,
        })

        add_another = input("Add another course? (y/n): ").strip().lower()
        if add_another not in {"y", "yes"}:
            break

    students.append({
        "first_name": first_name,
        "last_name": last_name,
        "courses": courses,
    })
    print(f"\nStudent '{first_name} {last_name}' was added successfully.")


def display_student(student, index=None):
    """Display one student's details and calculated GPA."""
    full_name = f"{student['first_name']} {student['last_name']}"
    prefix = f"{index}. " if index is not None else ""
    gpa = calculate_gpa(student)

    print(f"\n{prefix}{full_name}")
    print("-" * (len(prefix) + len(full_name)))
    for course in student["courses"]:
        print(
            f"  {course['name']}: grade {course['grade']:g}, "
            f"{course['units']} unit(s)"
        )
    print(f"  GPA: {gpa:.2f}")


def display_all_students(students):
    """Display every registered student."""
    if not students:
        print("\nNo students have been registered yet.")
        return

    print("\n========== All Students ==========")
    for index, student in enumerate(students, start=1):
        display_student(student, index)


def display_students_by_gpa(students):
    """Display students from highest GPA to lowest GPA."""
    if not students:
        print("\nNo students have been registered yet.")
        return

    ordered_students = sorted(
        students,
        key=lambda student: (
            -calculate_gpa(student),
            student["last_name"].casefold(),
            student["first_name"].casefold(),
        ),
    )

    print("\n========== Students by GPA ==========")
    for index, student in enumerate(ordered_students, start=1):
        full_name = f"{student['first_name']} {student['last_name']}"
        print(f"{index}. {full_name} — GPA: {calculate_gpa(student):.2f}")


def display_gpa_extreme(students, highest=True):
    """Display all students tied for the highest or lowest GPA."""
    if not students:
        print("\nNo students have been registered yet.")
        return

    target_gpa = (
        max(calculate_gpa(student) for student in students)
        if highest
        else min(calculate_gpa(student) for student in students)
    )
    title = "Highest" if highest else "Lowest"

    print(f"\n========== {title} GPA: {target_gpa:.2f} ==========")
    for student in students:
        if calculate_gpa(student) == target_gpa:
            print(
                f"- {student['first_name']} {student['last_name']} "
                f"(GPA: {target_gpa:.2f})"
            )


def display_conditional_students(students):
    """Display students whose GPA is below the conditional threshold."""
    if not students:
        print("\nNo students have been registered yet.")
        return

    conditional_students = [
        student
        for student in students
        if calculate_gpa(student) < CONDITIONAL_GPA_LIMIT
    ]

    print(
        f"\n========== Conditional Students "
        f"(GPA below {CONDITIONAL_GPA_LIMIT:g}) =========="
    )
    if not conditional_students:
        print("There are no conditional students.")
        return

    for student in conditional_students:
        print(
            f"- {student['first_name']} {student['last_name']} "
            f"(GPA: {calculate_gpa(student):.2f})"
        )


def search_by_last_name(students):
    """Find all students matching a last name and display their GPAs."""
    if not students:
        print("\nNo students have been registered yet.")
        return

    last_name = read_non_empty_text("Enter the student's last name: ")
    matches = [
        student
        for student in students
        if student["last_name"].casefold() == last_name.casefold()
    ]

    if not matches:
        print(f"No student found with last name '{last_name}'.")
        return

    print(f"\n========== Search Results: {last_name} ==========")
    for student in matches:
        print(
            f"- {student['first_name']} {student['last_name']} "
            f"(GPA: {calculate_gpa(student):.2f})"
        )


def display_menu():
    """Print the application menu."""
    print(
        "\n========== Student Grade Management System ==========\n"
        "1. Add Student\n"
        "2. Display All Students\n"
        "3. Display Students by GPA\n"
        "4. Display Highest GPA\n"
        "5. Display Lowest GPA\n"
        "6. Display Conditional Students\n"
        "7. Search Student by Last Name\n"
        "8. Exit"
    )


def main():
    """Run the application menu."""
    students = []

    while True:
        display_menu()
        choice = input("\nSelect an option (1-8): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            display_students_by_gpa(students)
        elif choice == "4":
            display_gpa_extreme(students, highest=True)
        elif choice == "5":
            display_gpa_extreme(students, highest=False)
        elif choice == "6":
            display_conditional_students(students)
        elif choice == "7":
            search_by_last_name(students)
        elif choice == "8":
            print("\nExiting Student Grade Management System.\nGoodbye!")
            break
        else:
            print("Invalid option. Please select a number from 1 to 8.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram interrupted. Goodbye!")
