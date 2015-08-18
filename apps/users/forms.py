from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile, Relationship
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Button, HTML
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            "first_name",
            "last_name",
            "email",
            'password1',
            'password2',
            ButtonHolder(
                HTML('<div class="g-recaptcha" data-sitekey="6Ld3bAcTAAAAAIWQXeG9RrOPyeG7GhBFF1Z_bl7r"></div><br>'),
                Submit('sign up', 'sign up', css_class='btn-success')
                ))


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('log in', 'log in', css_class='btn-success')))


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            ButtonHolder(
                Submit('Enter', 'Enter', css_class='btn-success'), Button('cancel', 'Cancel', onclick='window.history.back()')))


class RelationshipForm(ModelForm):
    class Meta:
        model = Relationship
        fields =['message']

    def __init__(self, *args, **kwargs):
        super(RelationshipForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'message',
            ButtonHolder(
                Submit('Enter', 'Enter', css_class='btn-success'), Button('cancel', 'Cancel', onclick='window.history.back()')))