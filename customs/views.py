from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from customs.models import Customs
from customs.paginators import CustomPagination
from customs.serializers import CustomSerializer
from users.permissions import IsOwner


class CustomsCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomSerializer
    queryset = Customs.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        custom = serializer.save()
        custom.owner = self.request.user
        custom.save()


class CustomsListAPIView(generics.ListAPIView):
    serializer_class = CustomSerializer
    queryset = Customs.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class CustomsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = CustomSerializer
    queryset = Customs.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class CustomsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomSerializer
    queryset = Customs.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class CustomsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = CustomSerializer
    queryset = Customs.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class CustomsPublicListAPIView(generics.ListAPIView):
    serializer_class = CustomSerializer
    queryset = Customs.objects.filter(is_public=True)
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
