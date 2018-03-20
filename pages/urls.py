from django.urls import path 

from . import views 

urlpatterns = [
    path('',views.HomePageView.as_view(), name='page'),
    path('about/',views.AboutPageView.as_view(),name = 'about'),
]