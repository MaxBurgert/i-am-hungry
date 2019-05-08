from django import forms

from cookbook.choices import PREPARATION_TIME_CHOICES, INGREDIENT_CHOICES


class RecipeForm(forms.Form):
    name = forms.CharField(label="Recipe name", max_length=100)
    ingredient_main = forms.ChoiceField(
        label="Main ingredient", choices=INGREDIENT_CHOICES, widget=forms.Select()
    )
    preparation_time = forms.ChoiceField(
        label="Preparation time",
        choices=PREPARATION_TIME_CHOICES,
        widget=forms.Select(),
    )
    vegetarian = forms.BooleanField(label="Vegetarian", required=False)
    source = forms.CharField(
        label="Recipe source", widget=forms.Textarea, max_length=100
    )


class DateSelectionForm(forms.Form):
    from_date = forms.DateField()
    to_date = forms.DateField()
