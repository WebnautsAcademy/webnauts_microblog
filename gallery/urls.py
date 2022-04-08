from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.PostList.as_view(), name='post_list'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='update_post'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='delete_post'),
    path('<int:pk>/likes/', views.post_likes, name='post_likes'),
    # path('create_post/', views.create_post, name='create_post'),
    path('create_post/', views.PostCreate.as_view(), name='create_post'),

]