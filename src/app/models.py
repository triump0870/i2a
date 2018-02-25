from __future__ import absolute_import

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django_extensions.db import fields as extension_fields
from django.core.urlresolvers import reverse
from django.conf import settings
from profiles.models import Profile

try:
    from django.contrib.auth import get_user_model

    User = settings.AUTH_USER_MODEL
except ImportError:
    from django.contrib.auth.models import User

OPTIONALITY_CHOICES = (
    ('optional', 'Optional'),
    ('mandatory', 'Mandatory')
)

REVIEW_CYCLE_CHOICES = (
    ('yearly', 'Yearly'),
    ('quarterly', 'Quarterly'),
    ('monthly', 'Monthly'),
    ('weekly', 'Weekly')
)


# Create your models here.
@python_2_unicode_compatible
class Owner(models.Model):
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    email = models.EmailField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    last_user = models.ForeignKey(Profile)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return "%s-%s" % (self.name, self.email)

    def get_absolute_url(self):
        return reverse('app_owner_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_owner_update', args=(self.slug,))


@python_2_unicode_compatible
class TagType(models.Model):
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    last_user = models.ForeignKey(Profile)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_tagtype_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_tagtype_update', args=(self.slug,))


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    type = models.ForeignKey(TagType)
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    last_user = models.ForeignKey(Profile)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('app_tag_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_tag_update', args=(self.slug,))


@python_2_unicode_compatible
class Application(models.Model):
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    description = models.TextField()
    logo = models.ImageField(blank=True, null=True)
    primary_owner = models.ForeignKey(Owner, related_name='primary_owner')
    secondary_owner = models.ForeignKey(Owner, related_name='secondary_owner')
    review_cycle = models.CharField(
        max_length=255,
        choices=REVIEW_CYCLE_CHOICES,
        blank=True,
        null=True)
    next_review_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    last_user = models.ForeignKey(Profile)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app_application_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('app_application_update', args=(self.slug,))


@python_2_unicode_compatible
class Rule(models.Model):
    text = models.TextField()
    optionality = models.CharField(
        max_length=50,
        choices=OPTIONALITY_CHOICES
    )
    weighting = models.IntegerField()
    review_cycle = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    factory_local_flag = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )
    version = models.IntegerField(
        blank=True,
        null=True
    )
    factory_reference = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )
    start_date = models.DateField(
        editable=True,
        blank=True,
        null=True
    )
    end_date = models.DateField(
        editable=True,
        blank=True,
        null=True
    )

    tag = models.ForeignKey(Tag)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    last_user = models.ForeignKey(Profile)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('app_rule_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('app_rule_update', args=(self.id,))


@python_2_unicode_compatible
class Questionnaire(models.Model):
    application_name = models.ForeignKey(Application)
    tagtype = models.ManyToManyField(TagType)
    tags = models.CharField(max_length=500)
    description = models.CharField(max_length=255)
    order = models.IntegerField()
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    last_user = models.ForeignKey(Profile)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.id

    def get_absolute_url(self):
        return reverse('app_questionnaire_detail', args=(self.id,))

    def get_update_url(self):
        return reverse('app_questionnaire_update', args=(self.id,))
