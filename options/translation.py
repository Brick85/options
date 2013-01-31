from modeltranslation.translator import translator, TranslationOptions
from options.models import Label, Text


class LabelTranslationOptions(TranslationOptions):
    fields = ('value',)
translator.register(Label, LabelTranslationOptions)


class TextTranslationOptions(TranslationOptions):
    fields = ('text', 'title')
translator.register(Text,  TextTranslationOptions)
