# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from phonenumber_field.modelfields import PhoneNumberField


from django.db import models

class User(models.Model):

    BRANCH=(
            ('AR', 'Architecture'),
            ('CE', 'Civil Engg.'),
            ('CH', 'Chemical Engg.'),
            ('CS', 'Computer Science'),
            ('EC', 'Electronics & Comm.'),
            ('EE', 'Electrical & Elec.'),
            ('ME', 'Mechanical Engg.'),
            ('PE', 'Production Engg.'),
            ('Other', 'Other')
    )
    
    register_no = models.CharField(max_length=8, primary_key=True, default='B14CS160')
    name = models.CharField(max_length=25)
    branch = models.CharField(choices=BRANCH, max_length=25, default='Other')
    phNo = models.IntegerField(default=0)



    def __str__(self):
        return self.name

class Item(models.Model):

    SEM=(
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4'),
        ('S5', 'S5'),
        ('S6', 'S6'),
        ('S7', 'S7'),
        ('S8', 'S8'),
        ('Other', 'Other')
    )

    BRANCH=(
        ('AR', 'Architecture'),
        ('CE', 'Civil Engg.'),
        ('CH', 'Chemical Engg.'),
        ('CS', 'Computer Science'),
        ('EC', 'Electronics & Comm.'),
        ('EE', 'Electrical & Elec.'),
        ('ME', 'Mechanical Engg.'),
        ('PE', 'Production Engg.'),
        ('Other', 'Other')
    )

    user_register_no = models.ForeignKey(User, on_delete=models.CASCADE, default='B14CS160')
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price= models.IntegerField(default=0)
    branch = models.CharField(choices=BRANCH, max_length=25, default='Other')
    sems = models.CharField(choices=SEM, max_length=6, default='S1')

    def __str__(self):
        return self.name
