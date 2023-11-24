from django.urls import path
from .views import ParentList, ParentDetail, ChildList, ChildDetail, ParentCreate, ChildCreate, ParentUpdate, \
    ChildUpdate, ParentDelete, ChildDelete

urlpatterns = [
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
