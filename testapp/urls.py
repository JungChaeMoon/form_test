from django.urls import path
from .views import PostCreateView, PostDetailView, PostListView

app_name = 'testapp'

urlpatterns = [
    path('list/', PostListView.as_view(), name='post_list'),
    path('list/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]