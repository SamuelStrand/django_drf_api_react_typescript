from django.urls import include, re_path, path
from django.views.decorators.cache import cache_page
from django_app import views
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Примеры маршрутов API",
        default_version="v1",
        # description="Test description",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"group", views.GroupViewSet)

app_name = "django_app"
urlpatterns = [
    re_path(r"^api/swagger(?P<format>\.json|\.yaml)/$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^api/swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^api/redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"api/", include(router.urls)),
    re_path(r"^index/$", cache_page(60 * 5)(views.HomeView.as_view()), name="index"),
    re_path(r"^home/$", cache_page(60 * 5)(views.HomeView.as_view()), name="home"),
    path("", cache_page(60 * 5)(views.HomeView.as_view()), name=""),
    path("chat/", views.rooms, name="rooms"),
    path("chat/<slug:slug>/", views.room, name="room"),
]
