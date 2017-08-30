from django.contrib import admin
from parse_wiki.models import Article, Section



class SectionInline(admin.StackedInline):
    model = Section
    readonly_fields = ('title',
                       'text',
                       'indicator',
                       'summarized',
                       'keywords',
                       )


class ArticleAdmin(admin.ModelAdmin):
    inlines = [SectionInline]
    model = Article
    readonly_fields = ('content_level',
                       'article_name',
                       )


class SectionAdmin(admin.ModelAdmin):

    model = Section
    readonly_fields = ('article',
                       'title',
                       'text',
                       'indicator',
                       'summarized',
                       'keywords',

                       )

    def has_add_permission(self, request):
        return False

admin.site.register(Article, ArticleAdmin)
admin.site.register(Section, SectionAdmin)
# Register your models here.
