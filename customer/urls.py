from django.urls import path

urlpatterns = [
    path("list/", CustomerListView.as_view(), name="customer-list")
]
