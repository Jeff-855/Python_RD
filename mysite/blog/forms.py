# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:56:30 2021

@author: Jack
"""

from django import forms
from .models import Test
class TestModelForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('test_id', 'name','salary')
        widgets = {
             'test_id' : forms.NumberInput(attrs={'class': 'form-control'}),
             'name' : forms.TextInput(attrs={'class': 'form-control'}),
             'salary': forms.NumberInput(attrs={'class': 'form-control'})
            
        }
        labels = {
            'test_id': '編號',
            'name': '姓名',
            'salary': '薪水',
            }