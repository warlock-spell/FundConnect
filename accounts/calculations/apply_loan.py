# @Project:     FundConnect
# @Filename:    apply_loan.py
# @Author:      Daksh Gaur
# @Email:       hi@daksh.fyi
# @Time:        25-06-2023 02:12 pm

from accounts.models import CashBookEntry


def check_eligibility(member, controller, loan):
    salary = member.monthly_salary
    salary_loan_ratio = controller.loan_monthly_salary_ratio_limit
    # sum of all loans + new loan
    loan_amount = loan.ask_loan_amount + member.loan
    return loan_amount <= salary * salary_loan_ratio


def allot_shares(member, controller, loan):
    loan_amount = loan.ask_loan_amount
    cumulative_loan_amount = loan_amount + member.loan
    current_share_holding = member.share_holding
    share_loan_ratio = controller.loan_share_holding_ratio_limit

    if current_share_holding * share_loan_ratio >= cumulative_loan_amount:
        loan.allotted_loan_amount = loan_amount
    else:
        increment_share_holding = (cumulative_loan_amount / share_loan_ratio) - current_share_holding
        loan.allotted_loan_amount = loan_amount - increment_share_holding
        member.share_holding += increment_share_holding
        member.save()

        # cashbook entry of share increment
        cashbook_entry, _ = CashBookEntry.objects.get_or_create(
            member=member,
            date=loan.date,
            month=loan.month,
            year=loan.year,
            fund_type='SHARES',
            refund_on_exit_amount=0,
            deposits_amount=0,
            loan_amount=0,
            shares_amount=increment_share_holding,
        )
        cashbook_entry.save()

    # save loan to database
    member.loan += loan.ask_loan_amount
    member.save()

    # cashbook entry
    cashbook_entry, _ = CashBookEntry.objects.get_or_create(
        member=member,
        date=loan.date,
        month=loan.month,
        year=loan.year,
        fund_type='LOAN',
        refund_on_exit_amount=0,
        deposits_amount=0,
        loan_amount=loan.ask_loan_amount,
    )
    cashbook_entry.save()

    return True
