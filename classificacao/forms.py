from django import forms

class UploadFileForms(forms.Form):
    arquivo = forms.FileField()

