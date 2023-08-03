from rest_framework import serializers
from django_api.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "description"]


class PostListSerializer(serializers.ModelSerializer):
    author_username = serializers.SerializerMethodField(read_only=True)

    def get_author_username(self, obj: Post) -> str:
        try:
            return obj.author.username
        except Exception as error:
            return ""

    class Meta:
        model = Post
        exclude = ["author"]


class PostUpdateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=300)
    description = serializers.CharField(max_length=3000)
    is_completed = serializers.BooleanField()
