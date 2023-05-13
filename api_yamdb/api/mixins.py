from rest_framework import mixins
from rest_framework import viewsets


class CreateListDestroyMixins(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
