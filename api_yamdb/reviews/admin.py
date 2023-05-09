from django.contrib import admin

<<<<<<< HEAD
from .models import Category, Genre, Review, Comment, Title
=======
from .models import User, Review, Comment
>>>>>>> 195b7f485ac51d552d4bcbdf8b2cc59af8b7c64c

admin.site.register(User)

class ReviewAdmin(admin.ModelAdmin):
    """Поля в Admin панели к отзывам"""

    list_display = (
        "id",
        "author",
        "title",
        "text",
        "score",
        "pub_date",
    )
    search_fields = ("text",)
    list_filter = (
        "score",
        "author",
        "pub_date",
    )
    empty_value_display = "-пусто-"


class CommentAdmin(admin.ModelAdmin):
    """Поля в Admin панели к коментариям к отзывам"""

    list_display = (
        "id",
        "author",
        "review",
        "text",
        "pub_date",
    )
    search_fields = ("text",)
    list_filter = (
        "author",
        "pub_date",
    )
    empty_value_display = "-пусто-"


class GenreAdmin(admin.ModelAdmin):
    """Поля в Admin панели к жанрам произведения"""
    list_display = ('id',
                    'name',
                    'slug',
                    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    """Поля в Admin панели к категориям произведения"""
    list_display = ('id',
                    'name',
                    'slug',
                    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    """Поля в Admin панели к названию произведения"""
    list_display = ('id',
                    'name',
                    'description',
                    'year',
                    'category',
                    )
    list_filter = ('name',
                   'year',
                   'category',
                   )
    search_fields = ('name',
                     'description',
                     )
    empty_value_display = '-пусто-'


admin.site.register(
    Review,
    ReviewAdmin,
)
admin.site.register(
    Comment,
    CommentAdmin,
)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
