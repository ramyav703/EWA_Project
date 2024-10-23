from django.db import models

class viewdata(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __str__(self):
		return self.name

class Order(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=200,default="Unknown Customer")
    card_number = models.CharField(max_length=16, default="0000000000000000")
    shipping_address = models.TextField(default="Unknown Address")
	
    def __str__(self):
        return f"Order {self.id} by {self.customer}"