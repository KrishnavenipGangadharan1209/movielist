import form
from django.forms import *
from django import forms
from  . models import *

class movieform(forms.ModelForm):

    class Meta:
        model=movlist
        fields=['moviename','moviedisc','Releaseyear','director','poster']

        widgets ={
            'moviename': forms.TextInput(attrs={'class':'form-control'}),
            'moviedisc': forms.TextInput(attrs={'class': 'form-control'}),
            'Releaseyear':forms.NumberInput(attrs={'class': 'form-control'}),
            'director': forms.TextInput(attrs={'class': 'form-control'}),
            'poster': forms.FileInput(attrs={'class': 'form-control'})
       }
