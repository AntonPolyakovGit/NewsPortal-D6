from django.urls import path
from .views import PostsList, PostDetail

urlpatterns = [
   path('news/', PostsList.as_view(), name='news'),
   path('news/<int:pk>', PostDetail.as_view(), name='new'),
]