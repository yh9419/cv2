from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'


# url, 뷰애 선언한 함수 , path 이름 설정
urlpatterns = [
    path('hello_world/', hello_world, name = 'hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name = 'create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name = 'update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name = 'delete'),
]