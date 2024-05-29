from blog import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('post/',views.PostListView.as_view(),name="post_list"),
    path('post/detail/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/delete/<int:pk>',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/create',views.PostCreateView.as_view(),name='post_create'),

]