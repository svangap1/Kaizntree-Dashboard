from django.urls import path
from . import views


urlpatterns = [
    # path('', views.get_data,name='all-data'),
    path('create/', views.create_item,name='all-data'),
    path('category/', views.CategoryManagement.as_view(),name='Category_Management'),
    path('html_view/', views.example_view, name='example'),
    # path('dashboard/', views.example_view, name='example'),
    path('',views.dashboard_view,name='dashboard'),

]



