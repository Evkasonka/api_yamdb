from rest_framework import serializers
from reviews.models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Review
        exclude = ("title",)
        read_only_fields = ("pub_date",)

    def validate(self, data):
        if self.context["request"].method != "POST":
            return data

        title_id = self.context["view"].kwargs.get("title_id")
        author = self.context["request"].user

        if Review.objects.filter(author=author, title=title_id).exists():
            raise serializers.ValidationError(
                "Можно публиковать только один отзыв на произведение"
            )

        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Comment
        exclude = ("review",)
        read_only_fields = ("review", "pub_date")
