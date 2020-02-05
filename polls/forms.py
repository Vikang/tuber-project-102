from django import forms

class SuggestionForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    body = forms.CharField(widget=forms.Textarea)
