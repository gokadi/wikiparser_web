from django.apps import AppConfig


class ParseWikiConfig(AppConfig):
    name = 'parse_wiki'

    def ready(self):
        import parse_wiki.signal_handlers
