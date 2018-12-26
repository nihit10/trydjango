from django.urls import path
from .views import post_list,post_detail,post_new,post_edit,post_delete,user_login,user_logout,register

urlpatterns = [
	path('', post_list, name='post_list'),
	path('post/<int:pk>/', post_detail, name='post_detail'),
	path('post/new/', post_new, name='post_new'),
	path('post/<int:pk>/edit/', post_edit, name='post_edit'),
	path('post/<int:pk>/delete/', post_delete, name='post_delete'),
	path('login/', user_login, name='user_login'),
	path('logout/', user_logout, name='user_logout'),
	path('register/', register, name='register'),
]
