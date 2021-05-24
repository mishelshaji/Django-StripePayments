from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('detail/<id>/', ProductDetailView.as_view(), name='detail'),
    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
    path('history/', OrderHistoryListView.as_view(), name='history'),

    path('api/checkout-session/<id>/', create_checkout_session, name='api_checkout_session'),
]