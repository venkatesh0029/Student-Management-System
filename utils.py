def validate_input(name, age, course):
    if not name or not course:
        return "Name and Course cannot be empty!"
    if not age.isdigit() or int(age) <= 0:
        return "Age must be a positive number!"
    return None
