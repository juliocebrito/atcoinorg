from django import forms
from django.forms import ModelForm
from .models import Entry, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder, Button, HTML

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['tittle', 'content', 'imageurl', 'image']

    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'tittle',
            'content',
            'imageurl',
            'image',
            ButtonHolder(
                Submit('Enter', 'Enter', css_class='btn-default'), Button('cancel', 'Cancel', onclick='window.history.back()')))


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'content',
            ButtonHolder(
                Submit('Enter', 'Enter', css_class='btn-default'), Button('cancel', 'Cancel', onclick='window.history.back()')))