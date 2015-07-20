from django.forms import widgets
from rest_framework import serializers
from .models import Entry, Comment

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('pk', 'tittle', 'content')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'content')