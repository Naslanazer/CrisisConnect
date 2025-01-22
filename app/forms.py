from django import forms

from .models import *

class disasterForm(forms.ModelForm):
    class Meta:
        model= DisasterTable
        fields=['Disaster','Details','Location','Weather', 'Image']
        
class resourcesForm(forms.ModelForm):
    class Meta:
        model= ResourceTable
        fields=['Name','Details','Quantity']


class NGORegForm(forms.ModelForm):
    class Meta:
        model= NGOTable
        fields=['Name','Email','Phone','Service', 'Specialization']

class taskForm(forms.ModelForm):
    class Meta:
        model= TaskTable
        fields=['Task_no','Task']

class ResourcelimitForm(forms.ModelForm):
    class Meta:
        model = Resourcelimit
        fields = ['resourcecategory', 'resourcelimit']