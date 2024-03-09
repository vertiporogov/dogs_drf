from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField

from dogs.models import Category, Dog


class DogListSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Dog
        fields = ('name', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    dog_count = IntegerField()
    class Meta:
        model = Category
        fields = ('name', 'dog_count',)


class CategoryDetailSerializer(serializers.ModelSerializer):
    dog_this_category = SerializerMethodField()

    def get_dog_this_category(self, category):
        return DogListSerializer(Dog.objects.filter(category=category), many=True).data

    class Meta:
        model = Category
        fields = '__all__'
