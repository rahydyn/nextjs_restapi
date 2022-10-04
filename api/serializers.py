from rest_framework import serializers
from .models import Task, Post, Answer
from django.contrib.auth.models import User
from tests.retrieve import retrieve_response


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')


class TaskSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')

    def create(self, request):
        print(request)
        form_id = '1AEjMA7Wxtn8yPHXIhxWUzig22f8JIURa60Rk-1ZnUCY'
        result = retrieve_response(form_id)
        print(result)
        task = Task(title=request["title"])
        task.save()
        return task


class AnswerSerializer(serializers.ModelSerializer):

    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'input_name', 'content', 'created_at')