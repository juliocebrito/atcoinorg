from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Entry(models.Model):
    user = models.ForeignKey(User)
    tittle = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20)
    content = models.CharField(max_length=200)
    image = models.URLField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "entry"
        verbose_name_plural = "entries"

    def __unicode__(self):
        return self.tittle

    def save(self, *args, **kwargs):
        self.slug = slugify(self.tittle)
        super(Entry, self).save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User)
    entry = models.ForeignKey(Entry)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __unicode__(self):
        return self.content