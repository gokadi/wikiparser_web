from unittest import skip

from django.test import TestCase
from parse_wiki.models import Article, Section


class TestArticle(TestCase):

    def test_url(self):
        self.assertEqual(self.article.url, 'https://en.wikipedia.org/wiki/Michael_Jackson')

    @skip
    def test_content(self):
        with open('parse_wiki/tests/test_article.txt', 'r') as f:
            self.assertEqual(self.article.content[:10000], f.read()[:10000])

    def test_soup_sections(self):
        h2, h3, h4, h5 = self.article.soup_sections()
        self.assertEqual(h2, self.h2)
        self.assertEqual(h3, self.h3)
        self.assertEqual(h4, [])
        self.assertEqual(h5, [])

    def test_wiki_sections(self):
        self.assertEqual(self.article.wiki_sections, self.wiki_sect)

    @skip
    def test_get_output(self):
        self.article.save()
        ch = self.article.get_output()
        print(ch[0])
        self.assertEqual(ch, 1)

    @classmethod
    def setUpTestData(cls):
        cls.article = Article(article_name='Michael Jackson', content_level='50')
        cls.h2 = ['Life and career', 'Death and memorial', 'Artistry', 'Legacy and influence',
                  'Honors and awards', 'Earnings and wealth', 'Discography', 'Filmography',
                  'Tours', 'See also', 'Notes', 'References', 'External links', 'Navigation menu']
        cls.h3 = ['1958–1975: Early life and the Jackson 5', '1975–1981: Move to Epic and Off the Wall',
                  '1982–1983: Thriller and Motown 25: Yesterday, Today, Forever',
                  '1984–1985: Pepsi, "We Are the World", and business career',
                  '1986–1990: Changing appearance, tabloids, Bad, films, autobiography, and Neverland',
                  '1991–1993: Dangerous, Heal the World Foundation, and Super Bowl XXVII',
                  '1993–1994: First child sexual abuse allegations and first marriage',
                  '1995–1997: HIStory, second marriage, and fatherhood',
                  '1997–2002: Label dispute and Invincible',
                  '2002–2005: Second child sexual abuse allegations and acquittal',
                  '2006–2009: Closure of Neverland, final years, and This Is It',
                  'Aftermath', 'Influences', 'Musical themes and genres', 'Vocal style',
                  'Music videos and choreography', "Net worth during Jackson's life",
                  'Net worth at time of death; U.S. federal estate tax problems',
                  'Earnings after death', 'Bibliography', 'Personal tools', 'Namespaces',
                  '\nVariants\n', 'Views', 'More', '\nSearch\n', 'Navigation', 'Interaction',
                  'Tools', 'Print/export', 'In other projects', 'Languages']
        cls.wiki_sect = ['Life and career', '1958–1975: Early life and the Jackson 5',
                         '1975–1981: Move to Epic and Off the Wall',
                         '1982–1983: Thriller and Motown 25: Yesterday, Today, Forever',
                         '1984–1985: Pepsi, "We Are the World", and business career',
                         '1986–1990: Changing appearance, tabloids, Bad, films, autobiography, and Neverland',
                         '1991–1993: Dangerous, Heal the World Foundation, and Super Bowl XXVII',
                         '1993–1994: First child sexual abuse allegations and first marriage',
                         '1995–1997: HIStory, second marriage, and fatherhood',
                         '1997–2002: Label dispute and Invincible',
                         '2002–2005: Second child sexual abuse allegations and acquittal',
                         '2006–2009: Closure of Neverland, final years, and This Is It',
                         'Death and memorial', 'Aftermath', 'Artistry', 'Influences',
                         'Musical themes and genres', 'Vocal style', 'Music videos and choreography',
                         'Legacy and influence', 'Honors and awards', 'Earnings and wealth',
                         "Net worth during Jackson's life",
                         'Net worth at time of death; U.S. federal estate tax problems', 'Earnings after death',
                         'Discography', 'Filmography', 'Tours', 'See also', 'Notes', 'References',
                         'Bibliography', 'External links']
