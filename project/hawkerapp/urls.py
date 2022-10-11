from . import views
from django.urls import path
urlpatterns = [
    path("", views.index, name="index"),
    path("registercustomer/", views.registercustomer, name="registercustomer"),
    path("registerhawker/", views.registerhawker, name="registerhawker"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("stallprofilehawker/<int:stall_id>", views.stallprofilehawker, name="stallprofilehawker"),
    path("stallprofilecustomer/<int:stall_id>", views.stallprofilecustomer, name="stallprofilecustomer"),
    path("hawkerprofile/", views.hawkerprofile, name="hawkerprofile"),
    path("customerprofile/", views.customerprofile, name="customerprofile"),
    path("addstall/", views.addstall, name="addstall"),
    path("addreview/<int:stall_id>", views.addreview, name="addreview"),
    path("resultspage/", views.resultspage, name="resultspage")
]