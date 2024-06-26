from django.urls import path
from rest_framework import routers

from dogs.apps import DogsConfig
from dogs.views.category import *
from dogs.views.dog import *

app_name = DogsConfig.name


urlpatterns = [
    path('', DogListAPIView.as_view(), name='list'),
    path('create/', DogCreateAPIView.as_view(), name='dog_create'),
    path('<int:pk>/update/', DogUpdateAPIView.as_view()),
    path('<int:pk>/', DogDetailAPIView.as_view()),
    path('<int:pk>/delete/', DogDeleteAPIView.as_view()),
    path('set_like/', SetLikeToDog.as_view()),
]

router = routers.SimpleRouter()
router.register('category', CategoryViewSet)

urlpatterns += router.urls
