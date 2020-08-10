from django.shortcuts import render
from django.shortcuts import redirect
from .models import Transaction
from . import views
from .forms import TransactionForm
# from blockchain import blockchain
from hashlib import sha256
import json
import time, requests
import datetime

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Create your views here.
def index(request):
    """  ___ __ ._`.*.'_._ ____ רףאל
        . +  * .\   o.* `.`. +.  א .
       *  .ת' '  \^/|  `. * .  * `
                 \V/ . +
        יהוה     /_\  .`.
       ======== _/W\_ =אדני:By: Two.0:.*"""

    context = {}
    return render(request, 'pages/blockchain.html', context)



def sign_Transaction(request):
    """  ___ __ ._`.*.'_._ ____ רףאל
        . +  * .\   o.* `.`. +.  א .
       *  .ת' '  \^/|  `. * .  * `
                 \V/ . +
        יהוה     /_\  .`.
       ======== _/W\_ =אדני:By: Two.0:.*"""
    finger_print = ''
    form = None
    if request.method == 'POST':
        form = TransactionForm(request.POST)
    if form.is_valid():
        date = form.cleaned_data['date']
        from_account = form.cleaned_data['from_account']
        to_account = form.cleaned_data['to_account']
        amount = form.cleaned_data['amount']
        notes = form.cleaned_data['notes']

        transaction = Transaction.objects.create(
                        date = date,
                        from_account = from_account,
                        to_account = to_account,
                        amount = amount,
                        notes = notes)
                        #
        finger_print = sha256(str(datetime.datetime.now()).encode('utf-8')+str(date).encode('utf-8')+str(from_account).encode('utf-8')+str(to_account).encode('utf-8')+str(amount).encode('utf-8')+str(notes).encode('utf-8')).hexdigest()

    context = {'fingerprint':finger_print}
    return render(request, 'pages/blockchain.html', context)

def sign_data(request):
    """  ___ __ ._`.*.'_._ ____ רףאל
        . +  * .\   o.* `.`. +.  א .
       *  .ת' '  \^/|  `. * .  * `
                 \V/ . +
        יהוה     /_\  .`.
       ======== _/W\_ =אדני:By: Two.0:.*"""
    finger_print = ''
    form = None
    if request.method == 'POST':
       form = Input_GoalForm(request.POST)
    if form.is_valid():
       goal = form.cleaned_data['goal']

       transaction = Transaction.objects.create(
                       goal = goal
                       )
                       #
       finger_print = sha256(str(goal).encode('utf-8')+str(datetime.datetime.now()).encode('utf-8')).hexdigest()
    context = {'fingerprint':finger_print}
    return render(request, 'pages/block_one.html', context)
