from django import forms
from .models import UserModel


class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['name', 'email']

    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = UserModel.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('email is taken')
        return email