from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from dogs.models import Dog
from dogs.serializers.category import DogListSerializer
from dogs.serializers.dog import DogSerializer, DogDetailSerializer


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogListAPIView(ListAPIView):
    serializer_class = DogListSerializer
    queryset = Dog.objects.all()


class DogDetailAPIView(RetrieveAPIView):
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()


class DogUpdateAPIView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDeleteAPIView(DestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
