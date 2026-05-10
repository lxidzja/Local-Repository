import unittest

from main import calculate_grade_statistics


class TestGradeStatistics(unittest.TestCase):

    def test_normal_case(self):
        grades = [
            {"name": "Олена", "grade": 95},
            {"name": "Олег", "grade": 45},
            {"name": "Марія", "grade": 70},
        ]
        result = calculate_grade_statistics(grades)
        self.assertEqual(result["average"], 70.0)
        self.assertEqual(result["highest"], 95)
        self.assertEqual(result["failed_students"], ["Олег"])

    def test_empty_list(self):
        result = calculate_grade_statistics([])
        self.assertEqual(result["average"], 0)
        self.assertEqual(result["highest"], 0)
        self.assertEqual(result["failed_students"], [])

    def test_all_failed(self):
        grades = [{"name": "Ігор", "grade": 50}, {"name": "Яна", "grade": 59}]
        result = calculate_grade_statistics(grades)
        self.assertEqual(result["highest"], 59)
        self.assertEqual(result["failed_students"], ["Ігор", "Яна"])

    def test_custom_passing_score(self):
        grades = [{"name": "Максим", "grade": 75}]
        result = calculate_grade_statistics(grades, passing_score=80)
        self.assertEqual(result["failed_students"], ["Максим"])


if __name__ == "__main__":
    unittest.main()
