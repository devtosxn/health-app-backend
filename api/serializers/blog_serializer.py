from rest_framework import serializers
from core.models.blogs import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','user_id','title', 'body', 'created_at', 'updated_at']

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'