from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name Here'})))
    last_name = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name Here'})))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control'})))
    last_name = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control'})))
    username = forms.CharField(max_length=100, widget=(forms.TextInput(attrs={'class': 'form-control'})))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})))
    new_password1 = forms.CharField(max_length=100, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})))
    new_password2 = forms.CharField(max_length=100, widget=(forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
