from django.urls import path
from snacks.views import AboutPageView, SnackDetailView, SnackListView

urlpatterns = [
  path("about/",AboutPageView.as_view(), name = "about"),
  path("",SnackListView.as_view(), name = "snack_list"),
  path("<int:pk>/",SnackDetailView.as_view(), name = "snack_detail")
]