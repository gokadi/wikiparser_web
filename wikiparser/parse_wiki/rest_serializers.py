from rest_framework import serializers
from parse_wiki.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    output = serializers.ReadOnlyField(source='get_output')

    class Meta:
        model = Article
        fields = ('article_name', 'content_level', 'output')
