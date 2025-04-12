from django.urls import path
from .views import ModelList, ModelDetail, increment_downloads, add_like,delete_like, toggle_comment

urlpatterns = [
    path('', ModelList.as_view(), name='models_list'),
    path('<int:pk>', ModelDetail.as_view(), name='models_detail'),
    path('<int:pk>/increment-downloads', increment_downloads, name='increment_downloads'),
    path('<int:pk>/like/add', add_like, name='add_like'),
    path('<int:pk>/like/delete', delete_like, name='delete_like'),
    path('<int:pk>/comment', toggle_comment, name='toggle_comment'),
]