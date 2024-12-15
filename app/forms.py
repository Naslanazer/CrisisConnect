from django import forms

from .models import *

class disasterForm(forms.ModelForm):
    class Meta:
        model= DisasterTable
        fields=['Disaster','Details','Location','Weather']
        
class resourcesForm(forms.ModelForm):
    class Meta:
        model= ResourceTable
        fields=['Name','Details','Quantity','Date']