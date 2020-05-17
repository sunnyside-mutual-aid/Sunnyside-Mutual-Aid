from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from modeltranslation.admin import TranslationAdmin

from .models import Page


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    list_display = ('title', 'published', 'order')
    list_editable = ('published', 'order')
    formfield_overrides = {
        'content': {'widget': AdminMartorWidget},
    }
