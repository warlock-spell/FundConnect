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


if __name__ == "__main__":
    test_get_financial_year()
