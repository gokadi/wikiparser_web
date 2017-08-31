from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from wikipedia.wikipedia import DisambiguationError
from parse_wiki.models import Article
from parse_wiki.rest_serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @list_route(methods=['get'])
    def show_sections(self, request, **kwargs):
        try:
            article, created = self.queryset.get_or_create(article_name=request.GET.get('title', 'Michael Jackson'),
                                                       content_level=request.GET.get('content_level', '50%')
                                                       )  # Title is the name of the article
        except DisambiguationError as e:
            return render(request, 'summ.html', {'summ': str(e),
                                                 'title': 'ERROR! BAD TITLE',
                                                 'content_level': 'ERROR! BAD TITLE'})
        return render(request, 'summ.html', {'summ': article.get_output(),
                                             'title': article.article_name,
                                             'content_level': article.content_level})
