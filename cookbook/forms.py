from django import forms


class RecipeForm(forms.Form):
    name = forms.CharField(label="Recipe name", max_length=100)
    ingredient_main = forms.CharField(label="Main ingredient", max_length=100)
    source = forms.CharField(
        label="Recipe source", widget=forms.Textarea, max_length=100
    )
