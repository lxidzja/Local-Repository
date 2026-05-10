import unittest

from main import add_service_fee, calculate_order_total, process_order


class TestCafeOrder(unittest.TestCase):

    def setUp(self):
        self.menu = {"кава": 45.0, "чай": 30.0, "круасан": 50.0, "салат": 120.0}

    def test_calculate_order_total_success(self):
        """Перевірка правильного підрахунку існуючих страв"""
        order = ["кава", "круасан"]
        result = calculate_order_total(order, self.menu)
        self.assertEqual(result, 95.0)

    def test_calculate_order_total_with_missing_item(self):
        """Перевірка, якщо страви немає в меню"""
        order = ["чай", "суп"]
        result = calculate_order_total(order, self.menu)
        self.assertEqual(result, 30.0)

    def test_calculate_order_total_empty(self):
        """Перевірка пустого замовлення"""
        result = calculate_order_total([], self.menu)
        self.assertEqual(result, 0.0)

    def test_add_service_fee(self):
        """Перевірка додавання чайових"""
        self.assertEqual(add_service_fee(100.0, 10.0), 110.0)
        self.assertEqual(add_service_fee(200.0, 5.0), 210.0)
        self.assertEqual(add_service_fee(50.0, 0.0), 50.0)

    def test_process_order(self):
        """Перевірка визначення остаточної суми замовлення"""
        order = ["салат", "чай"]
        result = process_order(order, self.menu, fee_percentage=10.0)
        self.assertEqual(result, 165.0)


if __name__ == "__main__":
    unittest.main()
