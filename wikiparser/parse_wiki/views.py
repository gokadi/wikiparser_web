from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from wikipedia.exceptions import DisambiguationError, PageError, WikipediaException
from parse_wiki.models import Article
from parse_wiki.rest_serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @list_route(methods=['get'])
    def show_sections(self, request, **kwargs):
        if request.GET.get('title') == '':
            return render(request, 'summ.html', {'summ': 'Title must be set',
                                                 'title': 'ERROR! BAD TITLE',
                                                 'content_level': 'ERROR! BAD TITLE'})
        try:
            try:
                article = self.queryset.get(article_name=request.GET.get('title'),
                                            content_level=request.GET.get('content_level'))
            except ObjectDoesNotExist:
                article = self.queryset.create(article_name=request.GET.get('title'),
                                               content_level=request.GET.get('content_level'))
        except DisambiguationError as e:
            self.queryset.filter(article_name=request.GET.get('title')).delete()
            return render(request, 'summ.html', {'summ': str(e),
                                                 'title': 'ERROR! BAD TITLE',
                                                 'content_level': 'ERROR! BAD TITLE'})
        except PageError as e:
            self.queryset.filter(article_name=request.GET.get('title')).delete()
            return render(request, 'summ.html', {'summ': str(e),
                                                 'title': 'ERROR! BAD TITLE',
                                                 'content_level': 'ERROR! BAD TITLE'})


        return render(request, 'summ.html', {'summ': article.get_output(),
                                             'title': article.article_name,
                                             'content_level': article.content_level})
