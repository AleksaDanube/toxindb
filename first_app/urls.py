from django.conf.urls import url
from django.urls import path
from . import views
# Create your views here.
app_name = "first_app"
urlpatterns = [
	url(r'^$', views.homepage, name = 'homepage'),
    url(r'^organisms/', views.organisms, name = 'organisms'),
    path(r'^organism_search/<str:organism>/', views.org_search, name='org_search'),
    path(r'^org_list_by_abc/<str:first_letter>/', views.org_list_by_abc, name='org_list_by_abc'),
    path(r'^pfam_search/<str:pfam>/', views.pfam_search, name='pfam_search'),
    ]
