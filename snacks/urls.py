from django.urls import path
from .views import SnackListView,SnackDetailView


urlpatterns=[
    path('', SnackListView.as_view(), name='snacks'),
    # path('snacks/', SnackListView.as_view(), name='snacks' )
    path('<int:pk>',SnackDetailView.as_view(), name='detail')
]