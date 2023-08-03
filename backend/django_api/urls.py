from django.urls import re_path
from django_api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "django_api"
urlpatterns = [
    re_path(r"token/$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    re_path(r"token/refresh/$", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"user/register/$", views.user_register_f, name="user_register_f"),
    re_path(r"post/create/$", views.post_create_f),  # C
    re_path(r"post/(?P<pk>\d+)/$", views.post_read_f),  # R
    re_path(r"post/list/$", views.post_list_f),  # R
    re_path(r"post/update/$", views.post_update_f),  # U
    re_path(r"post/(?P<pk>\d+)/delete/$", views.post_delete_f),  # D
]
