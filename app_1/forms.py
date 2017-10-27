from django import forms


class AddForm(forms.Form):
    name = forms.CharField(max_length=5)
    email = forms.EmailField(max_length=20)
    suggestion = forms.CharField(max_length=200)