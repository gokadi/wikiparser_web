from rest_framework import viewsets
from models import Article
from rest_serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    pass