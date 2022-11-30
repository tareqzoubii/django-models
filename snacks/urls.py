from django.urls import path
from .views import SnackListView


urlpatterns=[
    path('', SnackListView.as_view(), name='snacks'),
    # path('snacks/', SnackListView.as_view(), name='snacks' )
]