from rest_framework.serializers import ModelSerializer

from .models import ToDoList


class ToDoListSerializer(ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'
        read_only_fields = ('author', )


