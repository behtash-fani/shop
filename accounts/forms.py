from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    phone = forms.CharField(label='Phone Number ', widget=forms.NumberInput(attrs={'class': 'form-control mb-1'}))
    nickname = forms.CharField(label='Nickname ', widget=forms.TextInput(attrs={'class': 'form-control mb-1'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('phone','nickname')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone','email','nickname','first_name','last_name')
    
    def clean_password(self):
        return self.initial['password']

class LoginWithPwForm(forms.Form):
    phone = forms.CharField(label='Phone', widget=forms.NumberInput(attrs={'class':'form-control mb-1'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def phone_clean(self):
        phone = User.objects.filter(phone = self.cleaned_data['phone'])
        if not phone.exists():
            raise forms.ValidationError('This phone number does not exists, please enter currect phone number')
            return self.cleaned_data['phone']


class LoginWithCodeForm(forms.Form):
    phone = forms.CharField(label='Phone', widget=forms.NumberInput(attrs={'class':'form-control mb-1'}))

    def phone_clean(self):
        phone = User.objects.filter(phone = self.cleaned_data['phone'])
        if not phone.exists():
            raise forms.ValidationError('This phone number does not exists, please enter currect phone number')
            return self.cleaned_data['phone']

class VerifyCodeForm(forms.Form):
    code = forms.CharField(label='Enter code to verify', widget=forms.TextInput(attrs={'class':'form-control'}))