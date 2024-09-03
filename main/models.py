from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Product(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='pics', blank=True, null=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title

# class Image(models.Model):
#     img = models.ImageField(upload_to='pics')
#     service = models.ForeignKey(Product, on_delete=models.CASCADE)

class Image(models.Model):
    img = models.ImageField(upload_to='pics')
    service = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')





class ShoppingCart(models.Model):
    service = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_at = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.service.title} from {self.user.username}'

class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    STATUS = (
        (1, 'Created'),
        (2, 'Wait for payment'),
        (3, 'Paid'),
        (4, 'Delivering'),
        (5, 'Completed')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)

    def __str__(self):
        return f'{self.service.title} >>>> {self.status}'
