from rest_framework import viewsets

from dogs.models import Category
from dogs.serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
