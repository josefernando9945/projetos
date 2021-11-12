from django.urls import path

from instagran.views import UserlistViews

urlpatterns = [
    path('', UserlistViews.as_view(), name='list')
]