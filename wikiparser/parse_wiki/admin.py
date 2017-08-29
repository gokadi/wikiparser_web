from django.contrib import admin
from parse_wiki.models import Article, Section


class ArticleAdmin(admin.ModelAdmin):
    model = Article

class SectionAdmin(admin.ModelAdmin):
    model = Section
    readonly_fields = ('title',
                       'text',
                       'indicator',
                       'summarized',
                       'keywords',
                       )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)
# Register your models here.
