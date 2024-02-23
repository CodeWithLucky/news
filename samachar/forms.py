from . models import NewsModel
from django import forms

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = '__all__'
        widgets = {
            'date' : forms.DateInput(attrs =  {'type' : 'date'})
        } 
