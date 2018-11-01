from rest_framework import generics
from ..models import Category, Service, Seeker
from .serializers import CategorySerializer, ServiceSerializer, SeekerSerializer
from rest_framework import permissions
from rest_framework.response import Response
from .permission import IsOwnerOrReadOnly, IsProviderOrReadOnly, IsSeekerOrReadOnly


class parentCategory(generics.ListCreateAPIView):
    """
    Base API endpoint that shows all parent category and also accept post for authenticated user
    """
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()


class ServicesApi(generics.ListCreateAPIView):
    """
    Base API endpoint that display all services and new service can also be posted to it by authenticated user
    """
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()


class getParentCategoryServices(generics.ListCreateAPIView):
    """
    Base API endpoint that lists all services in a specified category and also accept new category
    """
    serializer_class = ServiceSerializer
    permission_classes = []

    def get_queryset(self, *args, **kwargs):
        query = self.kwargs.get("category_slug")
        if query is not None:
            qs = Service.objects.filter(category__slug=query)
            return qs


class NewSeeker(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = SeekerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(identity=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AllSeeker(generics.ListAPIView):
    serializer_class = SeekerSerializer
    permission_classes = []
    queryset = Seeker.objects.all()


class Seeker(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = SeekerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Seeker.objects.all()
