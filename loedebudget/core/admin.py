from django.contrib import admin
from .models import Expense

# Register your models here.
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'account', 'owner')
    search_fields = ('name', 'account', 'owner')
    list_filter = ('name', 'amount', 'owner')
    list_display_links = ('name', 'amount', )
    fields = ('owner', 'name', 'amount', 'account')

admin.site.register(Expense, ExpenseAdmin)