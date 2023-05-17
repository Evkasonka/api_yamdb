from rest_framework import mixins, viewsets


class CreateListDestroyMixins(mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet
                              ):
    pass
