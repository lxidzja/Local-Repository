def calculate_grade_statistics(grades: list[dict], passing_score: int = 60) -> dict:
    """
    Аналізує успішність студентів та повертає словник зі статистикою.

    >>> grades = [{'name': 'Іван', 'grade': 85}, {'name': 'Анна', 'grade': 92}, {'name': 'Петро', 'grade': 55}]
    >>> stats = calculate_grade_statistics(grades)
    >>> stats['average']
    77.33
    >>> stats['highest']
    92
    >>> stats['failed_students']
    ['Петро']
    >>> calculate_grade_statistics([])
    {'average': 0, 'highest': 0, 'failed_students': []}
    """
    if not grades:
        return {"average": 0, "highest": 0, "failed_students": []}

    total_score = 0
    highest_score = grades[0]["grade"]
    failed_students = []

    for student in grades:
        score = student["grade"]
        total_score += score

        if score > highest_score:
            highest_score = score

        if score < passing_score:
            failed_students.append(student["name"])

    average = round(total_score / len(grades), 2)

    return {
        "average": average,
        "highest": highest_score,
        "failed_students": failed_students,
    }


if __name__ == "__main__":
    import doctest

    print("Запуск doctests...")
    doctest.testmod(verbose=True)
