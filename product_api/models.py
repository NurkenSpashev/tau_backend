from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

CATEGORY = (
    ('relax', 'Для отдыха'),
    ('family', 'Для семьи'),
    ('friends', 'С друзьями'),
)


class Product(models.Model):
    name = models.CharField(max_length=255, help_text='Название', verbose_name='Название', db_index=True)
    price = models.CharField(max_length=255, help_text='Цена', verbose_name='Цена', db_index=True)
    description = models.TextField(help_text='Описание', verbose_name='Описание')
    address = models.CharField(max_length=255, help_text='Место положения', verbose_name='Место положения')
    category = models.CharField(max_length=50, choices=CATEGORY, default=CATEGORY[0])
    average_rating = models.FloatField(default=0, db_index=True)
    soft_delete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Владелец', verbose_name='Владелец')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукт'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def show_average(self):
        from django.db.models import Avg
        result = Comment.objects.filter(product=self).aggregate(Avg("rating"))
        return round(result["rating__avg"], 2)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментария'
        ordering = ['-pk']

    def __str__(self):
        return str(self.product) + "---" + str(self.user)

    def get_absolute_url(self):
        return reverse('comments_detail', kwargs={'pk': self.pk})


class Image(models.Model):
    title = models.CharField(max_length=255)
    path = models.ImageField(upload_to='uploads/products/%Y/%m/%d/', max_length=255)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, help_text='Продукт',
                                verbose_name='Продукты')
    soft_delete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Изображении'
        verbose_name_plural = 'Изображение'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Payment(models.Model):
    pass


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='Product')
    payment = models.OneToOneField(Payment, on_delete=models.PROTECT, verbose_name='Payment')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user__username}: {self.product__name}'

