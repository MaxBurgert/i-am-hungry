from django import forms

from cookbook.choices import PREPARATION_TIME_CHOICES, INGREDIENT_CHOICES


class RecipeForm(forms.Form):
    name = forms.CharField(label="Recipe name", max_length=100)
    ingredient_main = forms.ChoiceField(
        label="Main ingredient", choices=INGREDIENT_CHOICES, widget=forms.Select()
    )
    preparation_time = forms.ChoiceField(
        choices=PREPARATION_TIME_CHOICES, widget=forms.Select()
    )
    source = forms.CharField(
        label="Recipe source", widget=forms.Textarea, max_length=100
    )
