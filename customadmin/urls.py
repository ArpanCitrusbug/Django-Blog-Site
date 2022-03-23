from django.urls import path


from customadmin.views import *

urlpatterns= [
    path('customadmin/', DisplayView.as_view(), name="customadmin"),
]