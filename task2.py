from typing import Callable


def generator_numbers(text: str):
    for x in text.split(" "):
        try:
            yield float(x)
        except ValueError:
            pass


def sum_profit(text: str, func: Callable) -> float:
    result = 0
    for x in func(text):
        result += x
    return result


input_text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(input_text, generator_numbers)
print(f"Загальний дохід: {total_income}")
