from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index,name='home'),
    url(r'^signup/', views.UserSignUpView.as_view(),name = 'signup'),
    url(r'^login/', views.loginview,name = 'login'),
    url(r'^logout/', views.logoutview,name = 'logout'),
    url(r'^list/', views.lists,name = 'list'),	
]