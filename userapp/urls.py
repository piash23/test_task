from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import ParentList, ParentDetail, ChildList, ChildDetail, ParentCreate, ChildCreate, ParentUpdate, \
    ChildUpdate, ParentDelete, ChildDelete

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('parents/', ParentList.as_view(), name='parent-list'),
    path('parents/<int:pk>/', ParentDetail.as_view(), name='parent-detail'),
    path('parents/<int:parent_id>/children/', ChildList.as_view(), name='child-list'),
    path('children/<int:pk>/', ChildDetail.as_view(), name='child-detail'),
    path('parents/create/', ParentCreate.as_view(), name='parent-create'),
    path('children/create/', ChildCreate.as_view(), name='child-create'),
    path('parents/update/<int:pk>/', ParentUpdate.as_view(), name='parent-update'),
    path('children/update/<int:pk>/', ChildUpdate.as_view(), name='child-update'),
    path('parents/delete/<int:pk>/', ParentDelete.as_view(), name='parent-delete'),
    path('children/delete/<int:pk>/', ChildDelete.as_view(), name='child-delete'),
]
