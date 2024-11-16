from django.urls import path

import homepage.views

app_name = "homepage"
urlpatterns = [
    path("", homepage.views.Home.as_view(), name="main"),
]
