from django import forms  
from django.forms import ModelForm
from framework.models import Framework  

class FrameworkForm(forms.ModelForm):  
    class Meta:  
        model = Framework  
        fields = "__all__"  