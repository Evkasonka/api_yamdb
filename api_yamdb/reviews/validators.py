import re

from django.core.exceptions import ValidationError

REGEX_FOR_USERNAME = re.compile(r'^[\w.@+-]+')


def validate_username(name):
    """
    Валидирует имя пользователя с помощью регулярного выражения.

    Регулярное выражение '^[\w.@+-]+' соответствует строке, содержащей только буквы, цифры и символы @.+-_.
    """
    if name == 'me':
        raise ValidationError('Имя пользователя "me" использовать нельзя!')
    if not REGEX_FOR_USERNAME.fullmatch(name):
        raise ValidationError(
            'Можно использовать только буквы, цифры и "@.+-_".')
