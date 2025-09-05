from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'ingredients', 'steps', 'cooking_time_minutes')
        widgets = {
            'description': forms.Textarea(attrs={'rows':3}),
            'ingredients': forms.Textarea(attrs={'rows':6, 'placeholder':'1 cup flour\n2 eggs\n...'}),
            'steps': forms.Textarea(attrs={'rows':6, 'placeholder':'Step 1...\nStep 2...'}),
        }
