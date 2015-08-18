from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User)
    slug = models.SlugField(max_length=20)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    related = models.ManyToManyField(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detailprofile', kwargs={'slug': self.slug})

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            profile, new = Profile.objects.get_or_create(user=instance,
                                                         first_name=instance.first_name,
                                                         last_name=instance.last_name,
                                                         email=instance.email
                                                         )

class RelationshipManager(models.Manager):
    pass

class Relationship(models.Model):
    user = models.ForeignKey(User)
    profile = models.ForeignKey(Profile)
    message = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    objects = RelationshipManager()

    class Meta:
        unique_together = ('user', 'profile')
        verbose_name = 'Relationship'
        verbose_name_plural = 'Relationships'

    def __unicode__(self):
        return unicode(self.profile)


