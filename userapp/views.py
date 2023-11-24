from rest_framework import generics
from .models import Parent, Child
from .serializers import ParentSerializer, ChildSerializer, ParentCreateSerializer, ChildCreateSerializer
from django.shortcuts import get_object_or_404


class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ChildList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        return Child.objects.filter(parent__id=parent_id)

    def perform_create(self, serializer):
        parent_id = self.kwargs['parent_id']
        parent_instance = get_object_or_404(Parent, id=parent_id)
        serializer.save(parent=parent_instance)


class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer


class ParentCreate(generics.CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentCreateSerializer


class ChildCreate(generics.CreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildCreateSerializer


class ParentUpdate(generics.UpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentCreateSerializer


class ChildUpdate(generics.UpdateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildCreateSerializer


class ParentDelete(generics.DestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer


class ChildDelete(generics.DestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
