from django import forms


class UploadForm(forms.Form):
    name = forms.CharField()
    pic = forms.ImageField(required=False)
