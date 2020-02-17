# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    Token = models.CharField(max_length=24)

    def __str__(self):
        return '{}'.format(self.user)



class Expense(models.Model):
    text = models.CharField(blank=True, max_length=100)
    date = models.DateTimeField()
    amount = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.amount, self.text)

class Income(models.Model):
    text = models.CharField(blank=True, max_length=100)
    date = models.DateTimeField(blank=True)
    amount = models.BigIntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.amount, self.text)
