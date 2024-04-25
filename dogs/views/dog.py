from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from dogs.models import Dog
from dogs.paginators import DogPaginator
from dogs.permissions import IsModerator, IsDogOwner, IsDogPublic
from dogs.serializers.category import DogListSerializer
from dogs.serializers.dog import DogSerializer, DogDetailSerializer
from dogs.tasks import send_message_like
from users.models import User


class DogCreateAPIView(CreateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    # permission_classes = [AllowAny]


class DogListAPIView(ListAPIView):
    serializer_class = DogListSerializer
    queryset = Dog.objects.all()
    # permission_classes = [AllowAny]
    pagination_class = DogPaginator


class DogDetailAPIView(RetrieveAPIView):
    serializer_class = DogDetailSerializer
    queryset = Dog.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator | IsDogOwner | IsDogPublic]


class DogUpdateAPIView(UpdateAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    # permission_classes = [IsAuthenticated, IsModerator | IsDogOwner]


class DogDeleteAPIView(DestroyAPIView):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()
    # permission_classes = [IsAuthenticated, IsDogOwner]


class SetLikeToDog(APIView):

    def post(self, request):
        user = get_object_or_404(User, pk=request.data.get('user'))
        dog = get_object_or_404(Dog, pk=request.data.get('dog'))
        if dog.likes.filter(id=user.id).exists():
            return Response({"result": f"лайк для собаки {dog} УЖЕ добавлен от {user}"}, status=200)
        dog.likes.add(user)
        send_message_like.delay(user.id, dog.id)
        return Response({"result": f"лайк для собаки {dog} добавлен от {user}"}, status=200)
