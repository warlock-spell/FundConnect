# @Project:     FundConnect
# @Filename:    helper_functions.py
# @Author:      Daksh Gaur
# @Email:       hi@daksh.fyi
# @Time:        25-06-2023 02:16 pm

def get_financial_year(month: int, year: int) -> str:
    months_of_prev_financial_year = [1, 2, 3, '01', '02', '03', '1', '2', '3']
    return (
        f"{int(str(year)[:4]) - 1}-{str(year)[2:]}"
        if month in months_of_prev_financial_year
        else f"{str(year)[:4]}-{int(str(year)[2:]) + 1}"
    )


month_days = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}


def get_days_left_in_financial_year(date: int, month: int, year: int) -> int:
    financial_year = get_financial_year(month, year)
    # total days left from current date to 31st March
    # days left in current month
    days_left = 0 if date == 29 and month == 2 else month_days[str(month)] - date + 1
    months_index = [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]
    current_month_index = months_index.index(month)
    # days in remaining months
    for month in range(current_month_index + 1, len(months_index)):
        days_left += month_days[str(months_index[month])]
    return int(days_left)


def test_get_financial_year():
    print("Testing get_financial_year()...")
    assert get_financial_year(1, 2023) == "2022-23"
    assert get_financial_year(2, 2023) == "2022-23"
    assert get_financial_year(3, 2023) == "2022-23"
    assert get_financial_year(4, 2023) == "2023-24"
    assert get_financial_year(5, 2023) == "2023-24"
    assert get_financial_year(6, 2023) == "2023-24"
    assert get_financial_year(7, 2023) == "2023-24"
    assert get_financial_year(8, 2023) == "2023-24"
    assert get_financial_year(9, 2023) == "2023-24"
    assert get_financial_year(10, 2023) == "2023-24"
    assert get_financial_year(11, 2023) == "2023-24"
    assert get_financial_year(12, 2023) == "2023-24"
    assert get_financial_year(1, 2024) == "2023-24"
    assert get_financial_year(2, 2024) == "2023-24"
    assert get_financial_year(3, 2024) == "2023-24"


def test_get_days_left_in_financial_year():
    print("Testing get_days_left_in_financial_year()...")
    assert get_days_left_in_financial_year(1, 1, 2023) == 90
    assert get_days_left_in_financial_year(1, 2, 2023) == 59
    assert get_days_left_in_financial_year(1, 3, 2023) == 31
    assert get_days_left_in_financial_year(1, 4, 2023) == 365
    assert get_days_left_in_financial_year(1, 5, 2023) == 335
    assert get_days_left_in_financial_year(1, 6, 2023) == 304
    assert get_days_left_in_financial_year(1, 7, 2023) == 274
    assert get_days_left_in_financial_year(1, 8, 2023) == 243
    assert get_days_left_in_financial_year(1, 9, 2023) == 212
    assert get_days_left_in_financial_year(1, 10, 2023) == 182
    assert get_days_left_in_financial_year(1, 11, 2023) == 151
    assert get_days_left_in_financial_year(1, 12, 2023) == 121
    assert get_days_left_in_financial_year(11, 1, 2024) == 80
    assert get_days_left_in_financial_year(24, 8, 2024) == 220
    assert get_days_left_in_financial_year(29, 2, 2024) == 31


if __name__ == "__main__":
    test_get_financial_year()
    test_get_days_left_in_financial_year()
