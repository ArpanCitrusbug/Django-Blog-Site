from django.urls import path
from BlogAPI.views import *

urlpatterns = [
    #UserAPI
    path('userapi/', PostAPI.as_view()),
    path('userapi/<int:pk>', PostAPI.as_view()),

    #PostAPI
    path('postapi/', PostAPI.as_view()),
    path('postapi/<int:pk>', PostAPI.as_view()),

    #CategoryAPI
    path('categoryapi/', CategoryAPI.as_view()),
    path('categoryapi/<int:pk>', CategoryAPI.as_view()),
    ]