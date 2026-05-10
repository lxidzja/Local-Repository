import os

import sentry_sdk
from dotenv import load_dotenv

load_dotenv()

SENTRY_DSN = os.environ.get("SENTRY_DSN", "")
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        traces_sample_rate=1.0,
    )


def check_is_even(value: str) -> bool:
    """
    Перевіряє, чи є введене значення парним числом.
    Якщо значення не є цілим числом, генерує ValueError.

    >>> check_is_even("4")
    True
    >>> check_is_even("-10")
    True
    >>> check_is_even("7")
    False
    """
    try:
        number = int(value)
    except ValueError:
        raise ValueError(f"Помилка: '{value}' не є цілим числом.")

    return number % 2 == 0


def main():
    print("Введіть 'q' або 'exit' для виходу.")

    while True:
        user_input = input("Введіть ціле число: ").strip()

        if user_input.lower() in ["q", "exit"]:
            print("Вихід з програми.")
            break

        try:
            is_even = check_is_even(user_input)
            if is_even:
                print(f"Число {user_input} є парним.")
            else:
                print(f"Число {user_input} є непарним.")
        except Exception as e:
            sentry_sdk.capture_exception(e)


if __name__ == "__main__":
    main()
