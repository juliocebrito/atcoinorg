from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


class Account(models.Model):
    user = models.OneToOneField(User, null=True)
    holder = models.CharField(max_length=200)
    balance = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"

    def __unicode__(self):
        return self.holder

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            account, new = Account.objects.get_or_create(user=instance,
                                                         holder=instance.get_full_name())

class Pay(models.Model):
    user = models.ForeignKey(User, null=True)
    account = models.ForeignKey(Account, null=True)
    value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "pay"
        verbose_name_plural = "pays"

    def __unicode__(self):
        return self.account

    def get_absolute_url(self):
        return reverse('detail_pay', kwargs={'pk': self.pk})


class CodePay(models.Model):
    pay = models.ForeignKey(Pay)
    url = models.URLField()
    create = models.DateTimeField(auto_now_add=True, auto_now=False)

    @receiver(post_save, sender=Pay)
    def create_codepay(sender, instance, created, **kwargs):
        if created:
            codepay, new = CodePay.objects.get_or_create(pay=instance)


class Charge(models.Model):
    user = models.ForeignKey(User, null=True)
    account = models.ForeignKey(Account, null=True)
    value = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = "charge"
        verbose_name_plural = "charges"

    def __unicode__(self):
        return self.account

    def get_absolute_url(self):
        return reverse('detail_charge', kwargs={'pk': self.pk})


class CodeCharge(models.Model):
    pay = models.ForeignKey(Pay)
    url = models.URLField()
    create = models.DateTimeField(auto_now_add=True, auto_now=False)

    @receiver(post_save, sender=Charge)
    def create_codecharge(sender, instance, created, **kwargs):
        if created:
            codecharge, new = CodeCharge.objects.get_or_create(pay=instance)