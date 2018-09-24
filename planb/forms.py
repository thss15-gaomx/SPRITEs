from django import forms


class UploadForm(forms.Form):
    name = forms.CharField()
    width = forms.IntegerField()
    height = forms.IntegerField()
    pic = forms.ImageField(required=False)
