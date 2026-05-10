def calculate_order_total(ordered_items: list, menu: dict) -> float:
    """
    Обчислює загальну вартість замовлених страв на основі меню.

    >>> menu = {'кава': 40.0, 'чай': 30.0, 'торт': 60.0}
    >>> calculate_order_total(['кава', 'торт'], menu)
    100.0
    >>> calculate_order_total(['чай', 'вода'], menu) # 'вода' відсутня в меню
    30.0
    >>> calculate_order_total([], menu)
    0.0
    """
    total = 0.0
    for item in ordered_items:
        if item in menu:
            total += menu[item]
    return total


def add_service_fee(total_amount: float, fee_percentage: float = 10.0) -> float:
    """
    Додає сервісний збір до загальної суми замовлення.

    >>> add_service_fee(100.0, 10.0)
    110.0
    >>> add_service_fee(50.0, 0.0)
    50.0
    >>> add_service_fee(200.0, 15.0)
    230.0
    """
    return total_amount + (total_amount * fee_percentage / 100.0)


def process_order(
    ordered_items: list, menu: dict, fee_percentage: float = 10.0
) -> float:
    """
    Визначає остаточну суму замовлення

    >>> menu = {'кава': 40.0, 'чай': 30.0, 'торт': 60.0}
    >>> process_order(['кава', 'торт'], menu, 10.0)
    110.0
    """
    total_items_cost = calculate_order_total(ordered_items, menu)
    final_total = add_service_fee(total_items_cost, fee_percentage)
    return final_total


if __name__ == "__main__":
    import doctest

    print("Запуск doctests...")
    doctest.testmod(verbose=True)
