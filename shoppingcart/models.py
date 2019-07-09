from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('ED', 'Evening dresses'),
    ('WD', 'Wedding dresses'),
    ('OD', 'Occasion dresses'),
    ('MXD', 'Maxi dresses'),
    ('MND', 'Mini dresses'),
    ('PD', 'Party dresses'),
    ('ED', 'Cocktail dresses'),
    ('WD', 'Day dresses'),
    ('OD', 'Festival dresses')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

class Item(models.Model):
    """
    Item class with a title, price, category and label
    """
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)

    
    def __str__(self):
        return self.title

class OrderItem(models.Model):
    """
    OrderItem class that makes the connection between
    order and item
    """
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

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