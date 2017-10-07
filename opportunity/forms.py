from django import forms
from .models import opportunity, comment


class add_form(forms.ModelForm):
    class Meta:
        model = opportunity
        exclude = ['temp_applications']


class comment_form(forms.ModelForm):
    class Meta:
        model = comment
        exclude = ['post', 'commented_by']
