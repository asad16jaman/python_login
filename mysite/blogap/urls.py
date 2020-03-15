from django.urls import path

from .views import LoginFunc,LogoutFunc,CreationFunc

urlpatterns=[
    path('',LoginFunc.as_view(),name='homeView'),
    path('logout/',LogoutFunc.as_view(),name='logoutPage'),
    path('creatuser/',CreationFunc.as_view(),name='registration')
]