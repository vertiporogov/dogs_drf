from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from dogs.models import Dog
from dogs.permissions import IsModerator, IsDogOwner, IsDogPublic
from dogs.serializers.category import DogListSerializer
from dogs.serializers.dog import DogSerializer, DogDetailSerializer


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]


class DogListAPIView(ListAPIView):
    serializer_class = DogListSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated]


class DogDetailAPIView(RetrieveAPIView):
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner | IsDogPublic]


class DogUpdateAPIView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsDogOwner]


class DogDeleteAPIView(DestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    permission_classes = [IsAuthenticated, IsDogOwner]
