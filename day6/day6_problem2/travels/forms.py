from logging import PlaceHolder
from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '제주도',
                'maxlength': 10,
            }
        )
    )
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': '2022-02-22',
            }
        )
        )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': '2022-02-22',
            }
        )
        )
    class Meta:
        model = Travel
        fields = '__all__'
        # exclude = ('title',)
