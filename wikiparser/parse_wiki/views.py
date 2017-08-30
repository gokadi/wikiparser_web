from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from parse_wiki.models import Article
from parse_wiki.rest_serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @list_route(methods=['get'])
    def show_sections(self, request, **kwargs):
        article, created = self.queryset.get_or_create(article_name=request.GET['title'],
                                                       content_level=request.GET['content_level']
                                                       )  # Title is the name of the article
        if created:
            article.save()
        return Response(article.get_output())  # Returns JSON with summarized article
