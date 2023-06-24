# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import CashBookEntryForm
from .models import CashBookEntry
from member.models import Member
from django.db.models import Q, F, ExpressionWrapper, IntegerField


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
