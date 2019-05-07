from django import forms

from cookbook.choices import PREPARATION_TIME_CHOICES


class RecipeForm(forms.Form):
    name = forms.CharField(label="Recipe name", max_length=100)
    ingredient_main = forms.CharField(label="Main ingredient", max_length=100)
    preparation_time = forms.ChoiceField(
        choices=PREPARATION_TIME_CHOICES, widget=forms.Select()
    )
    source = forms.CharField(
        label="Recipe source", widget=forms.Textarea, max_length=100
    )
