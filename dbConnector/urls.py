from django.urls import path
from . import views

urlpatterns = [
    path("fetch-records/<str:classType>", views.FetchRecords.as_view()),
    path("update-record", views.UpdateRecord.as_view()),
    path("delete-record", views.DeleteRecord.as_view()),
    path("add-record", views.AddRecord.as_view()),
    path("fetch-single-record/<str:classType>/<int:id>", views.FetchSingleRecord.as_view())
]