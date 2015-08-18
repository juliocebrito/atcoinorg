from django import forms
from django.forms import ModelForm
from .models import Account, Pay, Charge
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Button, HTML


class PayForm(ModelForm):
    class Meta:
        model = Pay
        fields = ['value']

    def __init__(self, *args, **kwargs):
        super(PayForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'value',
            ButtonHolder(
                Submit('Enter', 'Enter', css_class='btn-default'), Button('cancel', 'Cancel', onclick='window.history.back()')))


class ChargeForm(ModelForm):
    class Meta:
        model = Charge
        fields = ['value']

    def __init__(self, *args, **kwargs):
        super(ChargeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'value',
            ButtonHolder(
                Submit('Enter', 'Enter', css_class='btn-default'), Button('cancel', 'Cancel', onclick='window.history.back()')))