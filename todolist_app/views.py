from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin,\
    CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import ToDoList
from .serializers import ToDoListSerializer
from .filters import ToDoListFilter


# Create your views here.


class ToDoListModelViewSet(ReadOnlyModelViewSet):
    """
    API для просмотра списка дел

    list:
    API для просмотра

    retrieve:
    API для конкретики
    """
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    filterset_class = ToDoListFilter

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset if self.request.user.is_authenticated else queryset.filter(public=True)

    # def list(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         notes = self.get_serializer(self.get_queryset(), many=True)
    #         return Response(notes.data)
    #     else:
    #         notes = self.get_serializer(self.get_queryset().filter(public=True), many=True)
    #         return Response(notes.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         return Response(status=status.HTTP_403_FORBIDDEN)
    #
    #     return super().retrieve(request, *args, **kwargs)


class ToDoListCreateViewSet(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer

    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer: ToDoListSerializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




