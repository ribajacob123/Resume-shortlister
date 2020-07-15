from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),

    #path('account/', views.accountSettings, name="account"),

    #path('products/', views.products, name='products'),
    #path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('skill/<str:pk_test>/', views.skill, name="skill"),
    path('addskills/', views.add_skills, name='add_skills'),
    path('jobpost/', views.jobpost, name='jobpost'),
    path('createprofile/', views.createprofile, name="createprofile"),
    #path('updateprofile/<str:pk>/', views.updateprofile, name="updateprofile"),
    #path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]