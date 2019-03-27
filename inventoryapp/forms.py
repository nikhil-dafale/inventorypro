from django import forms
from .models import *

class MetalForm(forms.ModelForm):
    class Meta:
        model=Metals
        fields=('type','date','price','status','issues')


class PlasticForm(forms.ModelForm):
    class Meta:
        model=Plastics
        fields=('type','date','price','status','issues')

class CompositeForm(forms.ModelForm):
    class Meta:
        model=Composites
        fields=('type','date','price','status','issues')