from django import forms

class SetTypeForm(forms.Form):
    type = forms.IntegerField()
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)