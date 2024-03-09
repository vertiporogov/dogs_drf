from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from dogs.models import Dog, Category
from dogs.serializers.category import CategoryDetailSerializer


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'





class DogDetailSerializer(serializers.ModelSerializer):
    category = CategoryDetailSerializer()
    dog_with_same_category = SerializerMethodField()

    def get_dog_with_same_category(self, dog):
        return Dog.objects.filter(category=dog.category).count()

    class Meta:
        model = Dog
        fields = ('name', 'category', 'dog_with_same_category')
