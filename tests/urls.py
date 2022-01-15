# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2014 by Łukasz Mierzwa
    :contact: l.mierzwa@gmail.com
"""
from django.urls import include, path
from django.contrib.auth.views import LoginView


login = LoginView.as_view()


nsurlpatters = [
    path('login2', login, name='login2_url'),
]


urlpatterns = [
    path('login', login, name='login_url'),
    path('login/<slug:slug>/', login, name='login_args_url'),
    path('login/user/<pk:user_id>/', login, name='login_kwargs_url'),
    path('ns/', include((nsurlpatters, 'ns'), namespace='ns')),
]
