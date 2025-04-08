from django.urls import path
from .views import ModelList, ModelDetail

urlpatterns = [
    path('', ModelList.as_view(), name='models_list'),
    path('<int:pk>', ModelDetail.as_view(), name='models_detail'),
]