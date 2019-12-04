from django import forms
from .models import Squirrel_attr

# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
class SquirrelForm(forms.Form):
    class Meta:
        model = Squirrel_attr
        fields = '__all__'
