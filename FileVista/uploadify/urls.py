# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login_view, name='login'),  # Custom login view
    path('logout/', views.logout_view, name='logout'),  
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Password reset view
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('upload/', views.upload_file, name='upload_file'),
    path('file/<int:file_id>/', views.file_details, name='file_details'),
    path('file/<int:file_id>/modify/', views.add_modification, name='add_modification'),
    path('video_feed', views.video_feed, name='video_feed'),
]
