from User_Module.models import UserModel as User, MusicModel, CommentModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'age', 'password', 'country']


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CommentModel
        fields = '__all__'
