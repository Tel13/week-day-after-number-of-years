from django.urls import path, include
from .views import MyView, GeeksCreateView, GeeksListView, GeeksDetailView, GeeksUpdateView, GeeksDeleteView


urlpatterns = [
    path('index/', MyView.as_view(), name="index"),
    path('create/', GeeksCreateView.as_view(), name="create"),
    path('listview/', GeeksListView.as_view(), name="listview"),
    path('detail_view/<int:pk>', GeeksDetailView.as_view(), name="detail_view"),
    path('update-view/<int:pk>', GeeksUpdateView.as_view(), name="update-view"),
    path('detail_view/<int:pk>/delete', GeeksDeleteView.as_view(), name="delete"),

]