from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'maxlength' : 10,
                'placeholder' : 'title',
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'content',
                'rows':5,
                'columns':50,
            }
        )
    )
    class Meta:
        model=Article
        fields='__all__'