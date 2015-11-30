from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


class Entry(models.Model):
    user = models.ForeignKey(User)
    tittle = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20)
    content = models.CharField(max_length=200)
    imageurl = models.URLField(blank=True)
    image = models.ImageField(upload_to='image')
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

    def get_absolute_url(self):
        return reverse('detailentry', kwargs={'slug': self.slug})


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