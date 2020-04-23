from modeltranslation.translator import register, TranslationOptions

from .models import Page


class AutoSlugTranslationOptions(TranslationOptions):
    def add_translation_field(self, field, translation_field):
        if hasattr(translation_field, 'populate_from'):
            translation_field.populate_from = '{}_{}'.format(
                translation_field.populate_from,
                translation_field.language
            )

        super().add_translation_field(field, translation_field)


@register(Page)
class PageTranslationOptions(AutoSlugTranslationOptions):
    fields = ('title', 'slug', 'meta_description', 'content')
    empty_values = {'slug': ''}
