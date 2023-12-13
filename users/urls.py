from django.urls import path
from .views import (
    UserCreateView,
    UserDetailView,
)

# login과 logout 등의 url을 구현하지 않은 이유는 JWT를 사용하기 때문. 
urlpatterns = [
    path('signup/', UserCreateView.as_view(), name = 'signup'),
    path('user/<int:pk>/', UserDetailView.as_view(), name = 'user_detail'),
]
