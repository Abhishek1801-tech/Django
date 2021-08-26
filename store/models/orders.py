
from  django.db import models
from .product import Product
from .customer import Customers
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers , on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=500, default='' , blank= False)
    phone = models.CharField(max_length=10, default='', blank= False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)



    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date')



