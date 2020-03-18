from django.urls import path, include
from rest_framework import routers
from myapi.views import UserViewSet, AccountViewSet, TransactionListViewSet, TransactionViewSet, CurrencyViewSet

app_name = "myapi"

router = routers.DefaultRouter()
urlpatterns = router.urls

urlpatterns = [
    path("user", UserViewSet.as_view()),
    path('account',AccountViewSet.as_view()),
    path('transactionList', TransactionListViewSet.as_view()),
    path('transaction', TransactionViewSet.as_view()),
    path('currency',CurrencyViewSet.as_view()),
]

urlpatterns += router.urls
