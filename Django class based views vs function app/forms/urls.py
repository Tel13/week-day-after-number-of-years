from django.urls import path, include
from . import views


urlpatterns = [
    path('forms/', views.home_view, name="home"),
    path('forms/display-data/', views.extract_data_from_forms, name="display-data"),
    path('forms/display-data/delete-data/<int:id>', views.delete_data_from_db, name="delete-data'"),
    path('forms/display-data/update-data/<int:id>', views.update_data_from_db, name="update-data'"),
    path('forms/display-data/update-data/update-data/<int:id>', views.update_record, name="update-record'"),
]