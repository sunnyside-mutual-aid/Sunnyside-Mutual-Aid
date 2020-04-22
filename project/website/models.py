from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from martor.models import MartorField


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', max_length=255)
    published = models.BooleanField()
    content = MartorField(blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', args=[self.slug])
