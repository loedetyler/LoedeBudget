from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Expense

def expense_list(request):
    entries_for_user = Expense.objects.filter(owner=request.user)
    context = {
        "expenses": entries_for_user,
    }
    return render(request, 'core/expense_list.html', context)

def add_expense(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        account = request.POST.get('account')
        owner = request.user

        entry = Expense(owner=owner, name=name, amount=amount, account=account)
        entry.save()

        return redirect("expenses")
    else:
        return HttpResponse("Invalid request method")