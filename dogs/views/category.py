from django.db.models import Count
from rest_framework import viewsets

from dogs.models import Category
from dogs.serializers.category import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    default_serializer = CategorySerializer
    serializers = {
        "list": CategoryListSerializer,
        "retrieve": CategoryDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.annotate(dog_count=Count('dog'))
        return super().list(request, *args, **kwargs)
