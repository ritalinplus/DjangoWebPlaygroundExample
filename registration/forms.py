from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from registration.models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        """Checks if email exists in database."""
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya esta registrado, prueba con otro.")

        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'biography', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'biography': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Biografía'}),
            'link': forms.URLInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Enlace'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        """Checks if email exists in database."""
        email = self.cleaned_data.get("email")

        # changed_data is a django structure with all modified data in form.
        if 'email' in self.changed_data and User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya esta registrado, prueba con otro.")

        return email