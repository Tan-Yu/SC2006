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
    path("addmenu/<int:stall_id>", views.addmenu, name="addmenu"),
    path("addreview/<int:stall_id>", views.addreview, name="addreview"),
    path("resultspagebysearchbar/", views.resultspagebysearchbar, name="resultspagebysearchbar"),
    path("location/<str:location_name>", views.location, name="location"),
    path("map/", views.map, name="map"),
    path("bbq/", views.bbq, name="bbq"),
    path("seafood/", views.seafood, name="seafood"),
    path("malay/", views.malay, name="malay"),
    path("indian/", views.indian, name="indian"),
    path("chinese/", views.chinese, name="chinese"),
    path("western/", views.western, name="western"),
    path("desserts/", views.desserts, name="desserts"),
    path("drinks/", views.drinks, name="drinks"),
]

