from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        user_check = User.objects.filter(mail=request.data['userMail']).first()
        if user_check is not None:
            user = User.object.get(mail = request.data['mail'], password = request.data['password'])
            serializer = self.get_serializer_class()(user)
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        # newest = self.get_queryset().order_by('created').last()
        # serializer = self.get_serializer_class()(newest)
        # return Response(serializer.data)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    @action(methods=['post'], detail=False)
    def make_transaction(self,request):
        user_check = User.objects.filter(user_id=request.data['userId']).first()

        if user_check is not None:
            data = {
                'origin_account': request.data['origin'],
                'destiny_account': request.data['destiny'],
                'amount': request.data['amount'],
                'description': request.data['description']
            }

            serializer = self.get_serializer_class()(data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                return Response(status = status.HTTP_400)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class TransactionListViewSet(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(methods=['post'], detail=False)
    def get_transactions(self,request):
        user_check = User.objects.filter(user_id=request.data['userId']).first()
        if user_check is not None:
            queryset1 = Transaction.objects.filter(origin_account = request.data['accountId'])
            queryset2 = Transaction.objects.filter(destiny_account = request.data['accountId'])
            result = queryset1.union(queryset2, all = False)
            serializer = self.get_serializer_class()(result, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        

class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @action(methods=['post'], detail=False)
    def get_accounts(self,request):
        user_check = User.objects.filter(user_id=request.data['userId']).first()
        if user_check is not None:
            queryset = Account.object.filter(user = request.data['userId'])
            serializer = self.get_serializer_class()(result, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
  


