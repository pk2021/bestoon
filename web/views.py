# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Income, Expense, Token, User
from datetime import datetime



@csrf_exempt
def submit_expense(request):

    print (request.POST)
    return JsonResponse({
    'status':'Ok'
    }, encoder=json.JSONEncoder)
'''
    this_token = request.POST.get('token',False)
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        now = datetime.now()

    Expense.objects.create(user=this_user, amount = request.POST['amount'],
                            text = request.POST['text'],date = now)
'''
