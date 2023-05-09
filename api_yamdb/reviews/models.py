from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Genre(models.Model):
    """Жанр произведения"""
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр произведения',
        help_text='Жанр произведения'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug для URL',
        help_text='Короткое имя для URL'
    )

    def __str__(self):
        return self.slug


class Category(models.Model):
    """Категории произведений"""

    name = models.CharField(
        max_length=256,
        verbose_name='Категория произведения',
        help_text='Категория произведения'
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug для URL',
        help_text='Короткое имя для URL'
    )

class User(AbstractUser):

    """Модель создания пользователя."""

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    role = models.CharField(
        verbose_name='Роль пользователя',
        max_length=10,
        choices=USER_ROLES,
        default='USER',
    )
    confirmation_code = models.CharField(
        verbose_name='Токен пользователя',
        max_length=100,
        blank=True,
        null=True,
    )

    @property
    def is_admin(self):
        """Проверка пользователя на наличие прав администратора."""
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        """Проверка пользователя на наличие прав модератора."""
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        """Проверка пользователя на наличие стандартных прав."""
        return self.role == self.USER

    class Meta:
        ordering = ('username',)

        def __str__(self):
            return self.username

class Title(models.Model):
    """Название произведения"""

    name = models.CharField(
        max_length=256,
        verbose_name='Название произведения',
        help_text='Название произведения'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='добавьте описание'
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        help_text='укажите год выпуска'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанр произведения',
        help_text='укажите жанр произведения',
        related_name='titles',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория произведения',
        help_text='укажите категорию произведения',
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Review(models.Model):
    """Отзывы к произведениям"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    text = models.TextField(
        verbose_name="Текст отзыва",
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        verbose_name="Рейтинг произведения",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "title",
                    "author",
                ],
                name="unique_title_author",
            )
        ]
        ordering = ("-pub_date",)
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Комментарии к отзывам"""

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField(
        verbose_name="Текст комментария",
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации",
    )

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.text
