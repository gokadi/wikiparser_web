from collections import OrderedDict
from django.db import models
import wikipedia
import json
from bs4 import BeautifulSoup


class Article(models.Model):
    CONTENT_CHOICES = (
        ('0%', 'No text'),
        ('25%', 'Quarter of text'),
        ('50%', 'Half of text'),
        ('75%', 'Three quarters of text'),
        ('100%', 'Full text'),
    )
    article_name = models.CharField(max_length=64, blank=False)
    content_level = models.CharField(max_length=3, choices=CONTENT_CHOICES)

    @property
    def url(self):
        return wikipedia.page(self.article_name).url

    @property
    def content(self):
        import requests
        response = requests.get(self.url)
        return response.content.decode()

    def soup_sections(self):
        soup = BeautifulSoup(self.content, 'lxml')
        get_section = lambda h: h.get_text().replace('[edit]', '')
        # We need below to differ sections from subsections
        h2 = [get_section(h2) for h2 in soup.findAll('h2') if get_section(h2) != 'Contents']
        h3 = [get_section(h3) for h3 in soup.findAll('h3') if get_section(h3) != 'Contents']
        h4 = [get_section(h4) for h4 in soup.findAll('h4') if get_section(h4) != 'Contents']
        h5 = [get_section(h5) for h5 in soup.findAll('h5') if get_section(h5) != 'Contents']
        return h2, h3, h4, h5

    @property
    def wiki_sections(self):
        return [BeautifulSoup(s, 'lxml').get_text() for s in wikipedia.page(self.article_name).sections]

    def get_output(self):
        # p_list = list()
        p_dict = OrderedDict()
        for section in self.sections.all():
            tmp = section.output()
            p_dict[tmp[0]] = tmp[1]
            # p_list.append(section.output())
        return json.dumps(p_dict, indent=2, ensure_ascii=False)

    def __repr__(self):
        return '<Article \'{}\'>'.format(self.article_name)

    def __str__(self):
        return 'Article \'{}\' Content_level {}'.format(self.article_name, self.content_level)


class Section(models.Model):

    title = models.CharField(max_length=64, blank=False)
    text = models.TextField()
    indicator = models.CharField(max_length=40, blank=False)
    summarized = models.TextField()
    keywords = models.TextField()
    article = models.ForeignKey(Article, related_name='sections')

    def output(self):
        return [self.title, self.summarized]

    def __repr__(self):
        return '<Section \'{}\' Article \'{}\'>'.format(self.title, self.article.article_name)

    def __str__(self):
        return 'Article: ' + self.article.article_name + '. Section: ' + self.title


