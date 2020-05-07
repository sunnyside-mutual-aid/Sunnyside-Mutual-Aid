from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from martor.models import MartorField


class PageManager(models.Manager):
    def published(self, request = None):
        """Show unpublished pages to staff"""
        if request and request.user.is_staff:
            return self

        return self.filter(published=True)


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', max_length=255)
    published = models.BooleanField()
    meta_description = models.TextField(
        help_text="Text for meta tag description and social cards (SEO)",
        blank=True,
        null=True
    )
    content = MartorField(blank=True, null=True)
    internal_notes = models.TextField(
        help_text="A place to leave notes &ndash; this won't show up on page.",
        blank=True,
        null=True
    )

    objects = PageManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page', args=[self.slug])
