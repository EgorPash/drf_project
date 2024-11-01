from django.urls import path
from customs.apps import CustomsConfig
from customs.views import CustomsListAPIView, CustomsCreateAPIView, CustomsUpdateAPIView, CustomsRetrieveAPIView, \
    CustomsDestroyAPIView, CustomsPublicListAPIView

app_name = CustomsConfig.name


urlpatterns = [
    path('customs/', CustomsListAPIView.as_view(), name='customs_list'),
    path('customs/<int:pk>/', CustomsRetrieveAPIView.as_view(), name='customs_retrieve'),
    path('customs/create/', CustomsCreateAPIView.as_view(), name='customs_create'),
    path('customs/<int:pk>/update/', CustomsUpdateAPIView.as_view(), name='customs_update'),
    path('customs/<int:pk>/delete/', CustomsDestroyAPIView.as_view(), name='customs_delete'),
    path('public/', CustomsPublicListAPIView.as_view(), name='public_list')
]