from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from parse_wiki.models import Article
from parse_wiki.rest_serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @detail_route(methods=['post'])
    def show_sections(self):
        return Response(self.serializer_class.output)
