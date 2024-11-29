from django.urls import include, path

urlpatterns = [
    path("graduation/", include("app_example.urls")),
]
