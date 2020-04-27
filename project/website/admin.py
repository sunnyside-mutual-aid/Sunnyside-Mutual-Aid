from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from modeltranslation.admin import TranslationAdmin

from .models import Page


@admin.register(Page)
class PageAdmin(TranslationAdmin):
    formfield_overrides = {
        'content': {'widget': AdminMartorWidget},
    }
