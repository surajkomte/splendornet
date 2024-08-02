from django import forms
from.models import reviewModel

class reviewModelForm(forms.ModelForm):
    class Meta:
        model=reviewModel
        fields="__all__"
