from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_app.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']  #


class UserDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):  # HyperlinkedModelSerializer
    class Meta:
        model = Group
        fields = '__all__'
