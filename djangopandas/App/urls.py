from django.urls import path
from App import views

urlpatterns = [
    path("", views.index, name="index"),
    path("import_csv_file/", views.import_csv_file, name="import_csv_file"),
]
