from wikipedia import wikipedia
from django.db.models.signals import post_save
from django.dispatch import receiver
from parse_wiki.models import Article, Section
from parse_wiki.backend import FrequencySummarizer


@receiver(post_save, sender=Article)
def get_sections(sender, instance, created, **kwargs):
    content = wikipedia.page(instance.article_name).content
    fs = FrequencySummarizer()
    if content.split('=')[0]:
        intro_text = content.split('=')[0]
        intro_summarized = fs.summarize(intro_text, instance.content_level)
        intro_keywords = fs.keywords(intro_text)
        Section.objects.create(title='Introduction',
                               text=intro_text,
                               indicator='Introduction',
                               summarized=intro_summarized,
                               keywords=intro_keywords,
                               article=instance
                               )

    for sect_name in instance.wiki_sections:
        text = wikipedia.page(instance.article_name).section(sect_name)
        h2, h3, h4, h5 = instance.soup_sections()
        if sect_name in h2:  # Indicator
            indicator = 'Section'
        elif sect_name in h3:
            indicator = 'Subsection'
        elif sect_name in h4:
            indicator = 'SubSubsection'
        elif sect_name in h5:
            indicator = 'SubSubSubsection'
        else:
            indicator = 'ERROR. No section %s' % sect_name

        fs = FrequencySummarizer()
        summarized = fs.summarize(text, instance.content_level)
        keywords = fs.keywords(text)
        Section.objects.create(title=sect_name,
                               text=text,
                               indicator=indicator,
                               summarized=summarized,
                               keywords=keywords,
                               article=instance
                               )
