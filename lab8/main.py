import sentry_sdk

sentry_sdk.init(
    dsn="dsn",
    traces_sample_rate=1.0,
)


def analyze_response_times(data: list) -> float:
    """
    Аналізує список часу відповіді: перевіряє типи даних і знаходить максимальне значення.
    """
    if not data:
        raise ValueError("Список часу відповіді не може бути порожнім.")

    for item in data:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError(
                f"Невірний тип даних: '{item}' (тип {type(item).__name__}). Всі значення мають бути числами."
            )

    return max(data)


if __name__ == "__main__":
    valid_data = [10.5, 20, 15.2, 8, 42.1]
    try:
        max_time = analyze_response_times(valid_data)
        print(f"Максимальний час відповіді (валідні дані): {max_time} мс")
    except Exception as e:
        print(f"Помилка: {e}")

    invalid_data = [10.5, "timeout", 15.2]

    try:
        analyze_response_times(invalid_data)
    except Exception as e:
        sentry_sdk.capture_exception(e)

    analyze_response_times(["crash", 1, 2])
