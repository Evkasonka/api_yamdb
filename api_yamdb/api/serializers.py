from rest_framework import serializers

from reviews.models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    """Отзывы к произведениям."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        exclude = ("title",)
        read_only_fields = ("pub_date",)
        model = Review

    def validate(self, data):
        """Проверка, чтобы был опубликован только один отзыв."""
        if self.context["request",].method != "POST":
            return data
        title_id = self.context["view",].kwargs.get(
            "title_id",
        )
        author = self.context["request",].user
        review = Review.objects.filter(
            author=author,
            title=title_id,
        )
        if review.exists():
            raise serializers.ValidationError(
                "Можно публиковать только один отзыв на произведение",
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Комментарии к отзывам."""

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        exclude = ("review",)
        read_only_fields = (
            "review",
            "pub_date",
        )
        model = Comment
