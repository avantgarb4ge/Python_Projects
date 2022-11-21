from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Create your views here.
def home(request):
    # retrieve Transaction Form
    form = TransactionForm(data=request.POST or None)
    # checks if request method is POST
    if request.method == 'POST':
        # if the form is submitted, retrieve which account the user wants to view
        pk = request.POST['account']
        # call balance function to render that account's Balance Sheet
        return balance(request, pk)
    # pass content to the template in a dictionary
    content = {'form': form}
    # add content of form to page
    return render(request, 'checkbook/index.html', content)


# this function will render the Create New Account page when requested
def create_account(request):
    # retrieve the Account form
    form = AccountForm(data=request.POST or None)
    # checks if request method is POST
    if request.method == 'POST':
        # check to see if the submitted form is valid and if so, save form
        if form.is_valid():
            form.save()
            # returns the user back to the home page
            return redirect('index')
    # saves content to the template as a dictionary
    content = {'form': form}
    # add content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function will render the Balance page when requested
def balance(request, pk):
    # retrieve the requested account using its primary key
    account = get_object_or_404(Account, pk=pk)
    # retrieve all of that account's transactions
    transactions = Transaction.Transactions.filter(account=pk)
    # create account total variable, starting with initial deposit value
    current_total = account.initial_deposit
    # create a dictionary into which transaction info will be placed
    table_contents = {}
    # loop through transactions and determine which is a deposit or withdrawal
    for t in transactions:
        if t.type == 'Deposit':
            # if deposit add amount to balance
            current_total += t.amount
            # add transaction and total to the dictionary
            table_contents.update({t: current_total})
        else:
            # if withdrawal subtract amount from balance
            current_total -= t.amount
            # add transaction and total to the dictionary
            table_contents.update({t: current_total})
    # pass account, account total balance, and transaction info to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the Transaction page when requested
def transaction(request):
    # retrieve the Transaction form
    form = TransactionForm(data=request.POST or None)
    # checks if request method is POST
    if request.method == 'POST':
        # check to see if the submitted form is valid and if so, save form
        if form.is_valid():
            # retrieve which account the transaction was for
            pk = request.POST['account']
            form.save()
            # renders balance of the accounts Balance Sheet
            return balance(request, pk)
    # pass content to the template as a dictionary
    content = {'form': form}
    # add content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
