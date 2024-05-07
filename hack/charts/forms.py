from django import forms


class chartForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)