
from django.urls import path
from .views import GetIdealUser, UserDetailAPI,RegisterUserAPIView


urlpatterns = [
  path('register',RegisterUserAPIView.as_view()),
  path("get-details",UserDetailAPI.as_view()),        # need Authentication
  path("ideal/user/",GetIdealUser.as_view(), name="get-ideal-user"),
]
