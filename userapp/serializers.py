from rest_framework import serializers
from .models import Parent, Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('first_name', 'last_name')


class ParentSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = ('id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code', 'children')


class ParentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ('id', 'first_name', 'last_name', 'street', 'city', 'state', 'zip_code')

class ChildCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ('id', 'first_name', 'last_name', 'parent')