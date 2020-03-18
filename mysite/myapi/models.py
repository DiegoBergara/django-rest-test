from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=60)
    password = models.CharField(max_length=16)

    def user_chack(self,id):
        try:
            user = User.objects.get(user_id = id)
            return True
        except User.DoesNotExist:
            return False

    def __str__(self):
        return f"{self.user_id} : {self.mail} , {self.password}"


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    origin_account = models.IntegerField()
    destiny_account = models.IntegerField()
    amount = models.IntegerField()
    description = models.CharField()
    date_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        origin = Account.objects.get(account_id = self.origin_account)
        receiver = Account.objects.get(account_id = self.destiny_account)
        if origin is not None and receiver is not None:
            receiver_currency = Currency.objects.get(currency_name = receiver.currency)
            if receiver_currency is not None:
                exchange_funds = self.amount * receiver.exchange_rate
                receiver.addFunds(exchange_funds)
                origin.removeFunds(self.amount)
                return super(Transaction, self).save(*args, **kwargs)
            else:
                return {'error' : 'true'}
        else:
            return {'error' : 'true'}

    def __str__(self):
        return f"{self.transaction_id} : {self.origin_account}, {self.destiny_account}, {self.amount}, {self.date_time}"


class Currency(models.Model):
    currency_name = models.CharField(max_length=5, primary_key=True)
    exchange_rate = models.FloatField()

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    funds = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete = models.CASCADE)

    def addFunds(self, amount):
        self.funds = self.funds + amount
        return self.save()

    def removeFunds(self, amount):
        self.funds = self.funds - amount
        return self.save()
        

    def __str__(self):
        return f"{self.account_id} : {self.user}, {self.funds}, {self.currency}"