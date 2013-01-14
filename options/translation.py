from modeltranslation.translator import translator, TranslationOptions
from options.models import Label, Text

class QOptionsTranslationOptions(TranslationOptions):
    fields = ('value',)

translator.register(Label, QOptionsTranslationOptions)
translator.register(Text,  QOptionsTranslationOptions)
