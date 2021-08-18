from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class SignInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text input-text--primary-style",
                "placeholder": "Enter Your Username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input-text input-text--primary-style",
                "placeholder": "Enter Your Password"
            }
        )
    )


class SignUpForm(forms.ModelForm):
    GENDER = (("0", "Male"), ("1", "Female"), ("2", "Others"))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text input-text--primary-style",
                "placeholder": "First Name"
            }
        )
    )
    # middle_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "input-text input-text--primary-style",
    #             "placeholder": "Middle Name"
    #         }
    #     )
    # )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text input-text--primary-style",
                "placeholder": "Last Name"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input-text input-text--primary-style",
                "placeholder": "User Name"
            }
        )
    )
    dob = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "input-text input-text--primary-style",
                "placeholder": "Date of Birth"
            }
        )
    )
    gender = forms.ChoiceField(
        choices=GENDER,

    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "input-text input-text--primary-style",
                "placeholder": "Email Address"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input-text input-text--primary-style",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "input-text input-text--primary-style",
            }
        )
    )

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'username', 'dob', 'gender', 'email', 'password1',
                  'password2')

