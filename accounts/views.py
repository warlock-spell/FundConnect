# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CashBookEntryForm
from .models import CashBookEntry, Cashbook
from branch.models import Branch
from dashboard.models import Controller
from member.models import Member
from django.db.models import Q, F, ExpressionWrapper, IntegerField, Prefetch


def home(request):
    return render(request, 'accounts/cashbook-home.html')


def create_cashbook_entry(request):
    if request.method == 'POST':
        form = CashBookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:cashbook-home')
    else:
        form = CashBookEntryForm()

    return render(request, 'accounts/create-entry.html', {'form': form})


def view_cashbook(request, pk, financial_year):
    # sorting the cashbook entries by year and month (From April to March)
    cashbook_entries = CashBookEntry.objects.filter(
        member__id=pk,
        cashbook__financial_year=financial_year
    ).annotate(
        year_month_expression=ExpressionWrapper(
            # Custom expression to sort the cashbook entries by year and month of the financial year
            # (From April to March)
            # For example, 03 2024 will be 202403, and 05 2023 will be 202304
            F('year') * 100 + F('month'),
            output_field=IntegerField()
        )
    ).order_by('year_month_expression')

    member = member = get_object_or_404(Member, id=pk)

    context = {
        'cashbook_entries': cashbook_entries,
        'member_id': pk,
        'financial_year': financial_year,
        'member': member,
    }
    return render(request, 'accounts/cashbook-view.html', context)


def view_all_cashbook(request):
    if request.method == 'POST':
        financial_year = request.POST.get('financial_year')
        cashbooks = Cashbook.objects.filter(financial_year=financial_year)

        cashbook_entries = CashBookEntry.objects.filter(
            cashbook__financial_year=financial_year
        ).select_related('cashbook', 'member').prefetch_related(
            Prefetch('member__cashbooks', queryset=Cashbook.objects.filter(financial_year=financial_year))
        ).annotate(
            year_month_expression=ExpressionWrapper(
                # Custom expression to sort the cashbook entries by year and month of the financial year
                # (From April to March)
                # For example, 03 2024 will be 202403, and 05 2023 will be 202304
                F('year') * 100 + F('month'),
                output_field=IntegerField()
            )
        ).order_by('year_month_expression')

        context = {
            'cashbooks': cashbooks,
            'financial_year': financial_year,
            'cashbook_entries': cashbook_entries,
        }

        return render(request, 'accounts/cashbook-all-members.html', context)

    return render(request, 'accounts/cashbook-all-search.html')


def search_cashbook(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        financial_year = request.POST.get('financial_year')

        # Redirect to the cashbook entry list URL with the member ID and financial year as parameters
        return redirect(reverse('accounts:cashbook-view', kwargs={'pk': member_id, 'financial_year': financial_year}))
    else:
        return render(request, 'accounts/cashbook-search.html')


def transaction_by_date(request, date, month, year):
    cashbook_entries = CashBookEntry.objects.filter(
        year=year,
        month=month,
        date=date
    )

    context = {
        'cashbook_entries': cashbook_entries,
    }

    return render(request, 'accounts/transaction-by-date.html', context)


def search_transactions(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        month = request.POST.get('month')
        year = request.POST.get('year')

        return redirect(reverse('accounts:transactions-view', kwargs={'year': year, 'month': month, 'date': date}))
    else:
        return render(request, 'accounts/transaction-search.html')


def create_branch_entry(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        month = request.POST.get('month')
        year = request.POST.get('year')

        branches = Branch.objects.all()
        controller = Controller.objects.all().first()
        members = Member.objects.all()
        members = members.filter(active_user=True)

        return redirect(reverse('accounts:cashbook-branches-list', kwargs={'year': year, 'month': month, 'date': date}))
    else:
        return render(request, 'accounts/branch-remittance-entry-create.html')


def list_branch_for_entry(request, date, month, year):
    branches = Branch.objects.all()
    controller = Controller.objects.all().first()
    members = Member.objects.all()
    members = members.filter(active_user=True)

    context = {
        'branches': branches,
        'controller': controller,
        'members': members,
        'date': date,
        'month': month,
        'year': year,
    }
    return render(request, 'accounts/branch-remittance-entry-list.html', context)


def create_entry_for_selected_branch(request, pk, date, month, year):
    branch = get_object_or_404(Branch, id=pk)
    controller = Controller.objects.all().first()
    members = Member.objects.filter(branch=branch)
    members = members.filter(active_user=True)

    # Create a cashbook entry for each member of the branch
    for member in members:
        # if the month is April
        if month == 4:
            # Opening balance Entry
            # month entry
            pass
        # if the month is March
        elif month == 3:
            # month entry
            # refund on exit interest entry
            # deposit interest entry
            # dividend entry
            # Closing balance Entry
            pass
        else:

            # loan emi
            emi = 0

            cashbook_entry = CashBookEntry(
                member=member,
                date=date,
                month=month,
                year=year,
                fund_type='SALARY',
                refund_on_exit_amount=controller.refund_on_exit_monthly_deposit,
                deposits_amount=member.wish_to_deposit,
                loan_amount=emi,
            )

            # make changes to database

            cashbook_entry.save()

    return redirect(reverse('accounts:cashbook-home'))
