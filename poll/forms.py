from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Pdf


class PdfForm(forms.ModelForm):
    class Meta:
        model = Pdf
        fields = ['title', 'address', 'tags']
        labels = {
            'title': '',
            'address': '',
            'tags': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={"class": "hk-input col-10 py-2", "placeholder": "File name"}),
            'address': forms.URLInput(attrs={"class": "hk-input col-10 py-2", "placeholder": "file link address"}),
            'tags': forms.TextInput(attrs={"class": "hk-input col-10 py-2",
                                           "placeholder": "biology, primary two,novel, ..."}),
        }


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'hk-input col-10 py-2', 'placeholder': 'First name'}))

    last_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'hk-input col-10 py-2', 'placeholder': 'Last name'}))

    username = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={'class': 'hk-input col-10 py-2', 'placeholder': 'Email address'}))

    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'hk-input col-10 py-2', 'placeholder': 'Password'}))

    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'hk-input col-10 py-2', 'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].label = ''
        self.fields['last_name'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
