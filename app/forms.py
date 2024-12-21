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