import locale
import pytest

locale.setlocale(locale.LC_ALL, '')


def calculate_tax(income):
    if income <= 100_000:
        tax_rate = 0.10
    elif 100_001 <= income <= 500_000:
        tax_rate = 0.15
    elif 500_001 <= income <= 1_000_000:
        tax_rate = 0.20
    else:
        tax_rate = 0.25

    tax_amount = income * tax_rate
    return tax_amount


def main():
    print("Калькулятор налога на доход физического лица")
    try:
        income_str = input("Введите годовой доход в рублях: ")
        income = locale.atof(income_str.replace(' ', ''))
        if income < 0:
            print("Доход не может быть отрицательным.")
        else:
            tax = calculate_tax(income)
            print(f"Сумма налога: {tax:,.2f} рублей")
    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите числовое значение.")


if __name__ == "__main__":
    main()


# Тесты с использованием pytest
@pytest.mark.parametrize("income, expected_tax", [
    (50_000, 5_000.0),
    (150_000, 22_500.0),
    (600_000, 120_000.0),
    (1_500_000, 375_000.0),
    (0, 0.0),
    (-50_000, -5_000.0),
    (-1, -0.10)
])
def test_calculate_tax(income, expected_tax):
    assert calculate_tax(income) == expected_tax


if __name__ == "__main__":
    pytest.main()
