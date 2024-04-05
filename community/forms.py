from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']

class JoinGroupForm(forms.Form):
    group_id = forms.CharField(max_length=100)
