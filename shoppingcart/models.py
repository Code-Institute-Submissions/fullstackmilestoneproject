from django.db import models
from django.conf import settings
from django.shortcuts import reverse

CATEGORY_CHOICES = (
    ('DR', 'Dresses'),
    ('SH', 'Shoes'),
    ('SU', 'Suits'),
    ('VL', 'Veils'),
    ('RN', 'Rings'),
    ('FL', 'Flowers'),
    ('HA', 'Hair Accessories'),
    ('BP', 'Bags & Purses'),
    ('NT', 'Neckties'),
    ('SH', 'Shirts'),
    ('BS', 'Belts & Sashes'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    """
    Item class that contains the details of an item
    """
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("product", kwargs={'slug': self.slug})
        
    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={'slug': self.slug})
        
    def get_remove_from_cart_url(self):
        return reverse("remove_from_cart", kwargs={'slug': self.slug})

class OrderItem(models.Model):
    """
    OrderItem class that makes the connection between
    order and item. Has a method that gets the total item
    price, a method that gets the total item discount price
    and another one that returns the amount of money saved.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
        
    def get_total_item_price(self):
        return self.quantity * self.item.price
    
    def get_total_item_discount_price(self):
        return self.quantity * self.item.discount_price
        
    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_item_discount_price()

class Order(models.Model):
    """
    Order class that contains the details of an order
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
