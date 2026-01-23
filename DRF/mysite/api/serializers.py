from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    published_date = serializers.DateTimeField(read_only=True)
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]