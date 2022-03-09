from django import forms
from .models import *


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Queries
        fields = ['url', 'format']
        widgets = {'url': forms.Textarea(attrs={'rows': 2, 'cols': 148}),
                   'format': forms.Select()}
