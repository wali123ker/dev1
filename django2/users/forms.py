from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

INPUT_CLASS = "block w-full px-4 py-2 mb-1 rounded-lg border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"

class CustomUserCreationForm(UserCreationForm):
    template_name = "user_registration_form_snippet.html"  

    username = forms.CharField(
        label="Nombre de usuario",
        help_text=UserCreationForm.base_fields['username'].help_text,
        widget=forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": "Tu nombre de usuario"})
    )
    password1 = forms.CharField(
        label="Contraseña",
        help_text=UserCreationForm.base_fields['password1'].help_text,
        widget=forms.PasswordInput(attrs={"class": INPUT_CLASS, "placeholder": "Contraseña"})
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={"class": INPUT_CLASS, "placeholder": "Repite la contraseña"})
    )

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": "Tu nombre de usuario"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": INPUT_CLASS, "placeholder": "Contraseña"})
    )