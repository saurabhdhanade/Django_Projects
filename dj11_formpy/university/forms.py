from django import forms

class FormBranch(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    dob=forms.DateField()
    
    