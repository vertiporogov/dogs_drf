from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView

from dogs.models import Dog
from dogs.serializers.dog import DogSerializer


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogListAPIView(ListAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDetailAPIView(RetrieveAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogUpdateAPIView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


class DogDeleteAPIView(DestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
