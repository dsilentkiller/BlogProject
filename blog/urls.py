from blog import views
from django.urls import path
urlpatterns = [
     path('', views.base, name='base'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('blog/',views.PostListView.as_view(),name="list"),
    path('post/detail/<int:pk>',views.PostDetailView.as_view(),name='detail'),
    path('post/delete/<int:pk>',views.PostDeleteView.as_view(),name='delete'),
    path('post/create',views.PostCreateView.as_view(),name='create'),

]