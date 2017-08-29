from rest_framework import serializers
from models import Article


class ArticleSerializer(serializers.ModelSerializer):

    sections = serializers.StringRelatedField(many=True)
    output = serializers.ReadOnlyField(source='get_output')

    class Meta:
        model = Article
        fields = ('article_name', 'content_level', 'output')
