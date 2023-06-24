from django.contrib import admin

# Register your models here
from .models import CashBookEntry, Cashbook

admin.site.register(Cashbook)


class CashBookEntryAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'month', 'year', 'fund_type', 'refund_on_exit_amount', 'deposits_amount', 'loan_amount', 'member',
        'cashbook')
    list_filter = (
        'date', 'month', 'year', 'fund_type', 'refund_on_exit_amount', 'deposits_amount', 'loan_amount', 'member',
        'cashbook')
    search_fields = (
        'date', 'month', 'year', 'fund_type', 'refund_on_exit_amount', 'deposits_amount', 'loan_amount', 'member',
        'cashbook')


admin.site.register(CashBookEntry, CashBookEntryAdmin)
